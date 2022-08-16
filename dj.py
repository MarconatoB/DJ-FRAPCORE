from audioop import findfactor
import os
import random

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
        file = open('bangers.txt', 'a')
        file.write(url + '\n')
        file.close()
        return

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

    global bangers_URL
    reader = open('bangers.txt')
    bangers_URL = list(reader)
    print('Imported ' + str(len(bangers_URL)) + ' bangers from bangers.txt')

@client.event
async def on_message(message):
    print('new message : ' + message.content)
    if message.author == client.user:
        return

    if message.content.startswith(';;play https://'):
        add_banger_if_new(message.content[7:])
    elif message.content.startswith(';;playnext https://'):
        add_banger_if_new(message.content[11:])

    if message.content.startswith('!list bangers'):
        response = ''
        for banger in bangers_URL:
            response = response + banger
        await message.channel.send(response)
    if message.content.startswith('!pick'):
        await message.channel.send(';;play ' + random.choice(bangers_URL))
        
client.run(TOKEN)