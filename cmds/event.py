from ast import keyword
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdate = json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content in (jdate["keyword"]) and msg.author != self.bot.user:
            await msg.channel.send('apple')

def setup(bot):
    bot.add_cog(Event(bot))