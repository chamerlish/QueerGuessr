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

def get_random_flag():
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

    if channel_id not in active_game_locks:
        active_game_locks[channel_id] = asyncio.Lock()

    async with active_game_locks[channel_id]:
        if channel_id in active_hint_tasks:
            for task in active_hint_tasks[channel_id]:
                task.cancel()
            await asyncio.gather(*active_hint_tasks[channel_id], return_exceptions=True)
            active_hint_tasks[channel_id] = []
        else:
            active_hint_tasks[channel_id] = []

        correct_answer, info = get_random_flag()
        
        # Support multiple image filenames
        images = info["image"] if isinstance(info["image"], list) else [info["image"]]
        chosen_image = random.choice(images)
        image_file = discord.File("./flags/" + chosen_image, filename=chosen_image)

        embed = discord.Embed(description="🌈 What flag is this?")
        embed.set_image(url="attachment://" + chosen_image)
        await ctx.send(embed=embed, file=image_file)

        active_flags[channel_id] = [k.lower() for k in info["keywords"]]
        print(f"[{ctx.channel.name}] Answer: {correct_answer}")

        async def send_hint(index, when_remaining):
            try:
                await asyncio.sleep(ROUND_TIMEOUT - when_remaining)
                if (
                    channel_id in active_flags
                    and index < len(info["hints"])
                    and info["hints"][index].strip() != ""
                ):
                    await ctx.send(f"💡 Hint: {info['hints'][index]}")
            except asyncio.CancelledError:
                return

        tasks = [
            asyncio.create_task(send_hint(0, ROUND_TIMEOUT / 1.5)),
            asyncio.create_task(send_hint(1, ROUND_TIMEOUT / 4)),
            asyncio.create_task(send_hint(2, ROUND_TIMEOUT / 8)),
        ]
        active_hint_tasks[channel_id].extend(tasks)

        await asyncio.sleep(ROUND_TIMEOUT / 2)

        if channel_id in active_flags:
            await ctx.send(f"⏳ {ROUND_TIMEOUT / 2}s have passed! That's like half the time...")

        await asyncio.sleep(ROUND_TIMEOUT / 2)

        if channel_id in active_flags:
            active_flags.pop(channel_id)
            for task in active_hint_tasks[channel_id]:
                task.cancel()
            await asyncio.gather(*active_hint_tasks[channel_id], return_exceptions=True)
            active_hint_tasks[channel_id] = []

            await ctx.send(f"⏰ Time's up! The correct answer was **{correct_answer}**.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

    channel_id = message.channel.id
    if channel_id in active_flags:
        guess = message.content.strip().lower()
        correct_keywords = active_flags[channel_id]
        if guess in correct_keywords:
            result_msg = await message.channel.send(
                f"Correct! {message.author.mention} was right, it actually was the **{correct_keywords[0].title()}** flag! Nice one team 🤓🎉"
            )
            await result_msg.add_reaction("🔁")
            del active_flags[channel_id]
            if channel_id in active_hint_tasks:
                for task in active_hint_tasks[channel_id]:
                    task.cancel()
                await asyncio.gather(*active_hint_tasks[channel_id], return_exceptions=True)
                active_hint_tasks[channel_id] = []
        elif guess != "!play":
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
            await start_game(ctx)
            print(f"[{channel.name}] {user.name} requested a replay.")
        else:
            await channel.send("⚠️ A game is already in progress!")

    elif str(reaction.emoji) == "❓":
        try:
            search = reaction.message.content.split("**")[1]
        except IndexError:
            search = None
        
        if search:
            definition = get_definition(search)
            definition_embed = discord.Embed(
                title=f"{search.title()}:",
                description=definition,
                url=f"https://www.urbandictionary.com/define.php?term={search}",
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
