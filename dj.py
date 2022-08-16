import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bangers_URL = []

def add_banger_if_new(url):
    if url in bangers_URL:
        return
    else:
        bangers_URL.append(url)
        return

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith(';;play https://'):
        add_banger_if_new(message.content[7:])
    elif message.content.startswith(';;playnext https://'):
        add_banger_if_new(message.content[11:])

    if message.content.startswith('!list bangers'):
        for banger in bangers_URL:
            await message.channel.send(banger)
        
client.run(TOKEN)