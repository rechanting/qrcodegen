import qrcode
import random
import discord
from discord.ext import commands

token = 'place_token_here'

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user.name} is ready')

@client.command()
async def qrgen(ctx, qrUrl):
    url = qrUrl
    img = qrcode.make(url)
    num = random.random()
    type(img)
    img.save(f'./qrcodeImgs/{num}.png')
    await ctx.reply(f'Here is the qrcode for {url}', file=discord.File(f'./qrcodeImgs/{num}.png'))

client.run(token)