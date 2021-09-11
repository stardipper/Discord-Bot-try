import os
import discord
import json
import random
from discord import channel
from discord.ext import commands
intents = discord.Intents.all()

with open('set.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

#mode='r'跟'r'是一樣的意思

bot=commands.Bot(command_prefix='?')
@bot.event
async def on_ready():
    print('test bot is on line')
    channel=bot.get_channel(int(jdata['testzone']))
    await channel.send('我也要來寫Discord Bot拉!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'延遲時間{round(bot.latency*1000)}毫秒')
@bot.command()
async def symbol(ctx):
    pic1=discord.File("D:\\vscode's workspace\\DidcordBot\\pic\\symbol.png")
    await ctx.send(file=pic1)
@bot.command()
async def meme(ctx):
    randompic=random.choice(jdata['meme'])
    pic=discord.File(randompic)
    await ctx.send(file=pic)
@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'{extension}')
    await ctx.send('load is done')
@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'{extension}')
    await ctx.send('unload is done')
@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'{extension}')
    await ctx.send('reload is done')

for filename in os.listdir('./cmds'):
    print (filename)
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata["token"])