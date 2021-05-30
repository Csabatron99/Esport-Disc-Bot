import discord
import string
import random

CLIENT = discord.Client()

TOKEN = 'TOKEN HERE'


@CLIENT.event
async def on_ready():
    print('Sikeres bejelentkezés {0.user}!'.format(CLIENT))

imgcode = ['https://imgur.com/t/dank_memes/obglZ5L', 'https://imgur.com/t/dank_memes/b3k4xyd', 'https://imgur.com/t/dank_memes/bmdfSM3','https://imgur.com/t/dank_memes/y2qVnMG','https://imgur.com/t/dank_memes/ri1x40j']

@CLIENT.event
async def on_message(message):
    if message.author == CLIENT.user:
        return
    if message.content.startswith('!Hi'):
        await message.channel.send('Halika :3 ')
    if message.content.startswith('!parancsok'):
        await message.channel.send('!hi \n'
                                   '!meme')
    if message.content.startswith('!meme'):  
        wrap = discord.Embed(title="", type="rich")
        img = imgcode[random.randint(0,4)]
        print(img)
        wrap.set_image(url=img)
        await message.channel.send(img)
        
        
CLIENT.run(TOKEN)
