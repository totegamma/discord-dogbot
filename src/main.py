import os
import discord
import aiohttp
import asyncio

BOT_TOKEN  = os.getenv('BOT_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

client = discord.Client(intents=discord.Intents.default())

async def post_dog(channel):
    print('Dog Time!')
    async with aiohttp.ClientSession() as session:
        response = await session.get('https://dog.ceo/api/breeds/image/random')
        dog = await response.json()

    await channel.send(dog['message'])

    with open('/tmp/healthy', 'a') as fp:
        pass

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    while True:
        await post_dog(channel)
        await asyncio.sleep(60)

client.run(BOT_TOKEN)

