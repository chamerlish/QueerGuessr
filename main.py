import discord
from discord.ext import commands
from flags import get_random_flag


# intents setup
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content for commands


client = commands.Bot(command_prefix='!', intents=intents)

@client.command()
async def send_image(ctx):
    print("Generating random flag image...")
    (name, flag) = get_random_flag()
    image = discord.File("./flags/" + flag, filename=flag)
    embed = discord.Embed(description="What flag is this?")
    embed.set_image(url="attachment://"+ flag)
    print(name)
    await ctx.send(embed=embed, file=image)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print(f"Received message: {message.content} from {message.author}")

    await client.process_commands(message)


from dotenv import load_dotenv
import os

load_dotenv()

client.run(os.getenv('TOKEN'))
