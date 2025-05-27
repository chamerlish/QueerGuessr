import discord
from discord.ext import commands


# intents setup
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content for commands


client = commands.Bot(command_prefix='!', intents=intents)

@client.command()
async def send_image(ctx):    
    embed = discord.Embed(description="What flag is this?")
    await ctx.send(embed=embed)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print(f"Received message: {message.content} from {message.author}")


from dotenv import load_dotenv
import os

load_dotenv()

client.run(os.getenv('TOKEN'))
