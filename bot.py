import discord
from discord.activity import Game
from discord.ext import commands
from discord import channel
import random
import json
import os

client=commands.Bot(command_prefix='?')

with open('j.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


@client.event
async def on_ready():
    print ("Bot is on line.")
    game=discord.Game('Bot at your service.')
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_member_join(member):
    print ("A member have join.")

@client.command()
async def ping(ctx):
    await ctx.send(f'延遲時間{round(client.latency*1000)}毫秒')
@client.command(aliases=['是非題','question'])
async def quest(ctx, *, question):#*後只能有一個變數，然後全部丟在同一個變數(*後那個)，否則一般遇到空白就會被當成兩個輸入
    ans=['Yes','No']
    await ctx.send(f'問題:{question}\n答案:{random.choice(ans)}')

@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount+1)
@client.command()
async def load(ctx,exten):
    client.load_extension(f'cogs.{exten}')
    await ctx.channel.send(f'\"{exten}\" has loaded')
@client.command()
async def unload(ctx,exten):
    client.unload_extension(f'cogs.{exten}')
    await ctx.channel.send(f'\"{exten}\" has unloaded')
@client.command()
async def reload(ctx,exten):
    client.reload_extension(f'cogs.{exten}')
    await ctx.channel.send(f'\'{exten}\' has reloaded')
@client.command()
async def meme(ctx):
    randompic=random.choice(jdata['meme'])
    pictures=discord.File(randompic)
    await ctx.send(file=pictures)
    
    


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(jdata['token'])
