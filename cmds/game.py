import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdate = json.load(jfile)

class Game(Cog_Extension):

    @commands.command()
    async def game(ctx):
        random_question = random.choice(jdate['question'])
        question = discord.File(random_question)
        await ctx.send(question)

def setup(bot):
    bot.add_cog(Game(bot))