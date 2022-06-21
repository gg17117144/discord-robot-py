import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdate = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def 圖片(ctx):
        random_pic = random.choice(jdate['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

    @commands.command()
    async def 網路圖片(ctx):
        random_pic = random.choice(jdate['url_pic'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))