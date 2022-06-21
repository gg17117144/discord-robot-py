import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio,datetime

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
       

        # async def interval():
            # await self.bot.wait_until_ready()
            # self.channel = self.bot.get_channel(978141255454306324)#設定詞為頻道(頻道id)
            # while not self.bot.is_closed():
                # await self.channel.send('嗨開始囉')#傳送訊息到頻道'嗨開始囉'
                # await asyncio.sleep(5) #等待5秒

        # self.bg_task = self.bot.loop.create_task(interval())

    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel:{self.channel.mention}')


def setup(bot):
    bot.add_cog(Task(bot))