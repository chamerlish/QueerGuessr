import discord
from discord.ext import commands
import asyncio
import random
from flags import flags  # Your flags dictionary

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=':3 ', intents=intents)

active_flags = {}
active_hint_tasks = {}  # channel_id -> list of asyncio.Tasks
active_game_locks = {}  # channel_id -> asyncio.Lock()

ROUND_TIMEOUT = 60
HINT_TIMES = [ROUND_TIMEOUT // 1.5, ROUND_TIMEOUT // 4, ROUND_TIMEOUT // 8]

async def get_random_flag():
    correct_answer = random.choice(list(flags.keys()))
    return correct_answer, flags[correct_answer]

@client.command()
async def play(ctx):
    embed = discord.Embed(
        title="🏳️‍🌈 Flag Guessing Game",
        description="Want to play a flag guessing game? React with ✅ to start!",
        color=discord.Color.purple()
    )
    message = await ctx.send(embed=embed)
    await message.add_reaction("✅")

    def check(reaction, user):
        return (
            user != client.user
            and str(reaction.emoji) == "✅"
            and reaction.message.id == message.id
        )

    try:
        reaction, user = await client.wait_for("reaction_add", timeout=60.0, check=check)
        await ctx.send(f"🎮 Game starting! Get ready, {user.mention} and everyone!")
        await start_game(ctx)
    except asyncio.TimeoutError:
        await ctx.send("⏳ No one reacted in time. Maybe next time!")

async def start_game(ctx):
    channel_id = ctx.channel.id

    # Debug: Check if game is already running
    if channel_id in active_flags:
        print(f"[DEBUG] Game already running in {ctx.channel.name}, skipping...")
        return

    if channel_id not in active_game_locks:
        active_game_locks[channel_id] = asyncio.Lock()

    async with active_game_locks[channel_id]:
        # Double-check inside the lock
        if channel_id in active_flags:
            print(f"[DEBUG] Game started by another process in {ctx.channel.name}, exiting...")
            return
            
        # Clean up any existing hint tasks
        if channel_id in active_hint_tasks:
            for task in active_hint_tasks[channel_id]:
                task.cancel()
            await asyncio.gather(*active_hint_tasks[channel_id], return_exceptions=True)
            active_hint_tasks[channel_id] = []
        else:
            active_hint_tasks[channel_id] = []

        # Get flag info
        correct_answer, info = await get_random_flag()
        print(f"[{ctx.channel.name}] Starting new game - Answer: {correct_answer}")

        # Prepare image
        images = info["image"] if isinstance(info["image"], list) else [info["image"]]
        chosen_image = random.choice(images)
        
        try:
            # Create file asynchronously or with error handling
            image_file = discord.File("./flags/" + chosen_image, filename=chosen_image)
            
            embed = discord.Embed(description="🌈 What flag is this?")
            embed.set_image(url="attachment://" + chosen_image)
            
            # Send the flag image immediately
            await ctx.send(embed=embed, file=image_file)
            
        except FileNotFoundError:
            await ctx.send(f"❌ Error: Flag image '{chosen_image}' not found!")
            return
        except Exception as e:
            await ctx.send(f"❌ Error loading flag image: {str(e)}")
            return

        # Set active flag AFTER successfully sending the image
        active_flags[channel_id] = [k.lower() for k in info["keywords"]]
        print(f"[{ctx.channel.name}] Game active with keywords: {active_flags[channel_id]}")

        # Schedule hints
        async def send_hint(index, delay):
            try:
                await asyncio.sleep(delay)
                if (
                    channel_id in active_flags
                    and index < len(info["hints"])
                    and info["hints"][index].strip() != ""
                ):
                    await ctx.send(f"💡 Hint: {info['hints'][index]}")
            except asyncio.CancelledError:
                pass

        # Create hint tasks with proper delays
        tasks = [
            asyncio.create_task(send_hint(0, ROUND_TIMEOUT / 1.5)),
            asyncio.create_task(send_hint(1, ROUND_TIMEOUT / 4)),
            asyncio.create_task(send_hint(2, ROUND_TIMEOUT / 8)),
        ]
        active_hint_tasks[channel_id].extend(tasks)

        # Schedule midgame message
        async def midgame_message():
            try:
                await asyncio.sleep(ROUND_TIMEOUT / 2)
                if channel_id in active_flags:
                    await ctx.send(f"⏳ {ROUND_TIMEOUT / 2}s have passed! That's like half the time...")
            except asyncio.CancelledError:
                pass

        midgame_task = asyncio.create_task(midgame_message())
        active_hint_tasks[channel_id].append(midgame_task)

        # Schedule game timeout
        async def game_timeout():
            try:
                await asyncio.sleep(ROUND_TIMEOUT)
                if channel_id in active_flags:
                    # Clean up
                    active_flags.pop(channel_id, None)
                    if channel_id in active_hint_tasks:
                        for task in active_hint_tasks[channel_id]:
                            task.cancel()
                        await asyncio.gather(*active_hint_tasks[channel_id], return_exceptions=True)
                        active_hint_tasks[channel_id] = []

                    await ctx.send(f"⏰ Time's up! The correct answer was **{correct_answer}**.")
            except asyncio.CancelledError:
                pass

        timeout_task = asyncio.create_task(game_timeout())
        active_hint_tasks[channel_id].append(timeout_task)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

    channel_id = message.channel.id
    if channel_id in active_flags:
        guess = message.content.strip().lower()
        correct_keywords = active_flags[channel_id]
        
        if guess.replace(" ", "") in [word.replace(" ", "") for word in correct_keywords]:
            result_msg = await message.channel.send(
                f"Correct! {message.author.mention} was right, it actually was the **{correct_keywords[0].title()}** flag! Nice one team 🤓🎉"
            )
            await result_msg.add_reaction("🔁")
            
            # Clean up game state
            active_flags.pop(channel_id, None)
            if channel_id in active_hint_tasks:
                for task in active_hint_tasks[channel_id]:
                    task.cancel()
                await asyncio.gather(*active_hint_tasks[channel_id], return_exceptions=True)
                active_hint_tasks[channel_id] = []
                
            await result_msg.add_reaction("❓")

        
        elif guess != client.command_prefix + "play":
            await message.add_reaction("❌")

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return
    
    channel = reaction.message.channel
    ctx = await client.get_context(reaction.message)

    if str(reaction.emoji) == "🔁":
        if channel.id not in active_flags:
            await channel.send(f"🔁 {user.mention} requested a replay! Starting a new round...")
            print(f"[{channel.name}] {user.name} requested a replay.")
            await start_game(ctx)
        else:
            await channel.send("⚠️ A game is already in progress!")

    elif str(reaction.emoji) == "❓":
        try:
            search = reaction.message.content.split("**")[1]
        except IndexError:
            search = None
        
        import urllib.parse

        if search:
            try:
                encoded_search = urllib.parse.quote(search)
                url = f"https://www.urbandictionary.com/define.php?term={encoded_search}"
            except IndexError:
                url = None
                return

            

            definition = get_definition(search)
            definition_embed = discord.Embed(
                title=f"{search.title()}:",
                description=definition,
                url=url,
                color=discord.Color.red()
            )
            await ctx.send(embed=definition_embed)
        else:
            await ctx.send("❓ Sorry, I couldn't find what you want to define.")


def get_definition(word):
    return flags.get(word, {}).get("description", "No definition found.")

import os
from dotenv import load_dotenv

load_dotenv()
client.run(os.getenv("TOKEN"))