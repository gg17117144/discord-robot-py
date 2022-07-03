import datetime
import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}ms')

    @commands.command()
    async def hi(self,ctx):
        await ctx.send('a55d')

    @commands.command()
    async def embed(self,ctx):
        embed=discord.Embed(title="我是電腦人", description="是我啦哈哈", color=0x00c0f0, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="咩")
        embed.set_thumbnail(url="https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2022/01/06/0/15112038.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600&w=930")
        embed.add_field(name="1", value="11", inline=False)
        embed.add_field(name="2", value="22", inline=False)
        embed.add_field(name="3", value="33", inline=False)
        embed.add_field(name="4", value="44", inline=False)
        embed.set_footer(text="你是誰?")
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)

    @commands.group()
    async def codetest(self,ctx):
        pass

    @codetest.command()
    async def apple(self,ctx):
        await ctx.send('apple')

    @codetest.command()
    async def banana(self,ctx):
        await ctx.send('banana')

    @codetest.command()
    async def water(self,ctx):
        await ctx.send('water')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):
        print(data.emoji)
        if str(data.emoji) == '🎉':
            print('yes')
            #await data.member.send('感恩')
            print(data.member)
            await data.member.send('感恩您沒有冷漠我,已讀我非常的感謝您！我好愛你:heart: ')

def setup(bot):
    bot.add_cog(Main(bot))