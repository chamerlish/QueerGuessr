import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

active_flags = {}
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
    correct_answer, info = get_random_flag()
    image = discord.File("./flags/" + info["image"], filename=info["image"])

    embed = discord.Embed(description="🌈 What flag is this?")
    embed.set_image(url="attachment://" + info["image"])
    await ctx.send(embed=embed, file=image)

    active_flags[ctx.channel.id] = [k.lower() for k in info["keywords"]]
    print(f"[{ctx.channel.name}] Answer: {correct_answer}")

    # Send hints in the background
    async def send_hint(index, when_remaining):
        await asyncio.sleep(ROUND_TIMEOUT - when_remaining)
        if ctx.channel.id in active_flags and index < len(info["hints"]):
            await ctx.send(f"💡 Hint: {info['hints'][index]}")

    asyncio.create_task(send_hint(0, ROUND_TIMEOUT / 1.5))   # 30s remaining (after 30s)
    asyncio.create_task(send_hint(1, ROUND_TIMEOUT / 4))   # 15s remaining (after 45s)
    asyncio.create_task(send_hint(2, ROUND_TIMEOUT / 8))   # 7.5s remaining (after 52.5s)

    # Wait until half-time
    await asyncio.sleep(ROUND_TIMEOUT / 2)

    await ctx.send(f"⏳ {ROUND_TIMEOUT / 2}s have passed! That's like half the time, and it's like double a quarter of the time, and it's like the 5 out of 6 minus the third of the full time, maybe you should try to guess and stop reading this stupid message")

    # Wait the rest of the time
    await asyncio.sleep(ROUND_TIMEOUT / 2)

    # Show the answer if still active
    if ctx.channel.id in active_flags:
        active_flags.pop(ctx.channel.id)
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

import os
from dotenv import load_dotenv
from flags import flags
import random


load_dotenv()
client.run(os.getenv("TOKEN"))
