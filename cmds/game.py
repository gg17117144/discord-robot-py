from __future__ import print_function
from calendar import c
from email import message_from_binary_file
from http.client import OK
import math
from multiprocessing.connection import Listener
from sqlite3 import connect
from turtle import listen
from types import MemberDescriptorType

import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdate = json.load(jfile)

class Game(Cog_Extension):

    @commands.command()
    async def math(self,ctx):
        player = ctx.author.voice.channel.members
        list1 = [1,2,3,4,5,6,7,8,9,10]
        l1 = random.sample(list1,7)
        pn = len(player)
        
        print(pn)
        print(l1)
        print(l1[0],player[0])
        #print(l1[1],player[1])
        await player[0].send(f'您的數字為：{l1[0]}')

        def check(m):
            return m.content == "ok" and m.channel == ctx.channel

        msg = await self.bot.wait_for("message", check=check)
        await ctx.send(f'{player[0]}的數字是：{l1[0]}')


    @commands.command()
    async def GD(self,ctx):
        random_question = random.choice(jdate["question"])
        question = random_question
        await ctx.send(question)

    @commands.command()
    async def GA(self,ctx):
        maxGA = 10
        minGA = 1
        random_player1 = random.randint(minGA,maxGA)
        random_player2 = random.sample(range(minGA,maxGA),k = 5)
        await ctx.send(random_player1)
        await ctx.send(random_player2)
    
    @commands.command()
    async def joinbot(self,ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
    @commands.command()
    async def leavebot(self,ctx):
        await ctx.voice_client.disconnect()



        
    @commands.command() #猜數字遊戲
    async def guess(self, ctx):
    # 檢查回傳的是否是同一個人(已及是否在同一個頻道)
        def check(number):
            return number.author == ctx.author and number.channel == ctx.message.channel
        global lowernumber
        global highernumber
    
        lowernumber = 1
        highernumber = 100
    
        number = random.randint(lowernumber, highernumber)
        print(number)
    
        await ctx.send('1-100，任意選一個數字')
    
        for i in range(0, 5):    
            response = await self.bot.wait_for('message', check = check)
        
            try : 
                guess = int(response.content) 
        
            except:
                await ctx.send("請輸入數字")
            
            if guess == number : 
                await ctx.send("猜對了")
                break
            
            if guess > 100 :
                await ctx.send("超過100，格式錯誤")
                
            if guess < number:
                lowernumber = guess
                await ctx.send(f"比 {lowernumber}大，比 {highernumber} 小")
                
            if guess > number :
                highernumber = guess
                await ctx.send(f"比 {lowernumber}大，比 {highernumber} 小")


   

    async def game(ctx):
        random_question = random.choice(jdate['question'])
        question = discord.File(random_question)
        await ctx.send(question)

def setup(bot):
    bot.add_cog(Game(bot))