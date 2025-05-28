import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
from flags import flags
import random

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

active_flags = {}  # channel_id: accepted answers
game_tasks = {}    # channel_id: asyncio.Task to handle timers

ROUND_TIMEOUT = 60
HINT_DELAY = ROUND_TIMEOUT // 2

def get_random_flag():
    correct_answer = random.choice(list(flags.keys()))
    return correct_answer, flags[correct_answer]

@client.command()
async def play(ctx):
    embed = discord.Embed(
        title="🏳️‍🌈 Flag Guessing Game",
        description="Want to play a flag guessing game?\nReact with ✅ to start!",
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
    old_task = game_tasks.get(ctx.channel.id)
    if old_task:
        old_task.cancel()

    correct_answer, info = get_random_flag()
    image = discord.File("./flags/" + info["image"], filename=info["image"])

    embed = discord.Embed(description="🌈 What flag is this?")
    embed.set_image(url="attachment://" + info["image"])
    await ctx.send(embed=embed, file=image)

    active_flags[ctx.channel.id] = [k.lower() for k in info["keywords"]]
    print(f"[{ctx.channel.name}] Answer: {correct_answer}")

    game_tasks[ctx.channel.id] = asyncio.create_task(
        handle_timer(ctx, correct_answer, info.get("hint", "No hint available."))
    )

async def handle_timer(ctx, correct_answer, hint):
    try:
        await asyncio.sleep(HINT_DELAY)
        if ctx.channel.id in active_flags:
            await ctx.send(f"💡 Hint: {hint}")

        await asyncio.sleep(HINT_DELAY)
        if ctx.channel.id in active_flags:
            del active_flags[ctx.channel.id]
            await ctx.send(f"⏰ Time's up! The correct answer was **{correct_answer}**.")
    except asyncio.CancelledError:
        pass

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
            game_tasks[channel_id].cancel()
        elif guess != "!play":
            await message.add_reaction("❌")

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return

    if str(reaction.emoji) == "🔁":
        channel = reaction.message.channel

        if channel.id not in active_flags:
            ctx = await client.get_context(reaction.message)
            await channel.send(f"🔁 {user.mention} requested a replay! Starting a new round...")
            await start_game(ctx)
        else:
            await channel.send("⚠️ A game is already in progress!")

load_dotenv()
client.run(os.getenv("TOKEN"))
