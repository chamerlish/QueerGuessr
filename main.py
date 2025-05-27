import discord
from discord.ext import commands
from flags import get_random_flag

# intents setup
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content for commands

client = commands.Bot(command_prefix='!', intents=intents)

# Active flag answers per channel (one game per channel)
active_flags = {}  # channel_id: correct_answer


@client.command()
async def send_image(ctx):
    print("Generating random flag image...")
    (name, flag) = get_random_flag()
    image = discord.File("./flags/" + flag, filename=flag)

    embed = discord.Embed(description="🌈 What flag is this? 🌈")
    embed.set_image(url="attachment://" + flag)

    await ctx.send(embed=embed, file=image)

    # Save the correct answer for this channel (lowercase for easy comparison)
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
            await message.channel.send(
                f"✅ Correct! {message.author.mention} was right, It actually the was**{correct_answer.title()}** flag! Nice one team 🤓🎉"
            )
            del active_flags[channel_id]  # End the game
        else:
            await message.add_reaction("❌")  # Optional feedback


from dotenv import load_dotenv
import os

# Load token from .env
load_dotenv()

client.run(os.getenv("TOKEN"))
