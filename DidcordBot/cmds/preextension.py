import discord
import json
import random
from discord.ext import commands
from discord.ext.commands import cog

class ex1 (commands.cog):
    def __init__(self, bot):
        self.bot=bot