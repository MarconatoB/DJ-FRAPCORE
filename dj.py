import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')



async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == ';;play':
        return

bot.run(TOKEN)