#from DidcordBot.extension.preextension import ex1
import discord
import json
import random
from discord.ext import commands
from core.classes import Cog_Extension





from discord.ext.commands import cog
#這很重要，難怪程式一直沒把這看成cog

from test import bot

with open('set.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class names(Cog_Extension):
    
    
    @commands.cog.listener()
    async def on_member_join(member):
        channel=bot.get_channel(int(jdata['mainchannel']))
        await channel.send(f'{member} join!')
    @commands.cog.listener()
    async def on_member_remove(member):
        channel=bot.get_channel(int(jdata['mainchannel']))
        await channel.send(f'{member} left!')
    @commands.command()
    async def check(self,ctx):
        await ctx.send("unready")

def setup(bot):
    bot.add_cog(names(bot))