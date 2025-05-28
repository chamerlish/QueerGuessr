import discord
from discord.ext import commands
from flags import get_random_flag
import asyncio


# intents setup
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content for commands

client = commands.Bot(command_prefix='!', intents=intents)

# Active flag answers per channel (one game per channel)
active_flags = {}  # channel_id: correct_answer


@client.command()
async def play(ctx):
    # Send invitation embed
    embed = discord.Embed(
        title="🏳️‍🌈 Flag Guessing Game",
        description="Want to play a flag guessing game?\nReact with ✅ to start!",
        color=discord.Color.purple()
    )
    message = await ctx.send(embed=embed)
    await message.add_reaction("✅")

    def check(reaction, user):
        return (
            user != client.user and
            str(reaction.emoji) == "✅" and
            reaction.message.id == message.id
        )

    try:
        reaction, user = await client.wait_for("reaction_add", timeout=60.0, check=check)
        await ctx.send(f"🎮 Game starting! Get ready, {user.mention} and everyone!")
        await start_game(ctx)
    except asyncio.TimeoutError:
        await ctx.send("⏳ No one reacted in time. Maybe next time!")

async def start_game(ctx):
    print("Generating random flag image...")
    (name, flag) = get_random_flag()
    image = discord.File("./flags/" + flag, filename=flag)

    embed = discord.Embed(description="🌈 What flag is this?")
    embed.set_image(url="attachment://" + flag)

    await ctx.send(embed=embed, file=image)

    active_flags[ctx.channel.id] = name.lower()
    print(f"[{ctx.channel.name}] Answer: {name}")

@client.event
async def on_message(message):
    # Ignore the bot's own messages
    if message.author == client.user:
        return

    # Process commands first
    await client.process_commands(message)

    # Get the channel ID
    channel_id = message.channel.id

    # Only respond if a game is active in this channel
    if channel_id in active_flags:
        user_guess = message.content.strip().lower()
        correct_answer = active_flags[channel_id]

        if user_guess == correct_answer:
            result_msg = await message.channel.send(
                f"Correct! {message.author.mention} was right, It actually the was **{correct_answer.title()}** flag! Nice one team 🤓🎉"
            )
            await result_msg.add_reaction("🔁")
            del active_flags[channel_id]

        elif user_guess != "!play":
            await message.add_reaction("❌")  # Optional feedback

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return

    if str(reaction.emoji) == "🔁":
        channel = reaction.message.channel

        # Start new game if none active
        if channel.id not in active_flags:
            ctx = await client.get_context(reaction.message)
            await channel.send(f"🔁 {user.mention} requested a replay! Starting a new round...")
            await start_game(ctx)
        else:
            await channel.send("⚠️ A game is already in progress!")


from dotenv import load_dotenv
import os

# Load token from .env
load_dotenv()

client.run(os.getenv("TOKEN"))
