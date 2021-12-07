import discord
import os
import time
from datetime import datetime
import asyncio
import datetime as dt
from discord.ext import commands, tasks

bot = commands.Bot("$")
client = discord.Client()
TOKEN = os.getenv('DTOKEN')
GUILD = os.getenv('GTOKEN')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#on boot
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

        



@client.event
#code 1 = check credits
#code 3 = +credits
#code 6 = -credits
#code 7 = help
#code 12 = check others credits
#code 9 Clear messages
#triggers once a message is sent
async def on_message(message):
    #If message is sent by a user not bot
    if message.author == client.user:
        person = (message.author)

        return (person)
#Once command +credits is used
    if message.content.startswith('+credits') and discord.utils.get(
            message.author.roles, name="Credditor"):
        person = (message.author.id)
        await message.delete()
        await message.channel.send('Cwedits added')
        print('code 3')
        credit = message.content
        scredit = list(credit.split())
        scredit.remove(scredit[0])
        amnt = scredit.pop(0)
        user = (scredit)
        print(amnt)
        print(credit)
        print(user)
        amnts = int(amnt)
        username = str(user)
        print(username)
        file1 = open("@!" + (username) + ".txt", "a")
        file1.close
        file1 = open("@!" + (username) + ".txt", "r")
        cr = file1.read()
        cr = int(float(cr))
        total = amnts + cr
        file1.close
        file1 = open("@!" + (username) + ".txt", "w")
        total = str(total)
        file1.write(total)
        return person, credit
#when command -credit is used
    if message.content.startswith('-credits') and discord.utils.get(
            message.author.roles, name="Credditor"):
        person = (message.author.id)
        await message.delete()
        await message.channel.send('Cwedits wost')
        print('code 6')
        credit = message.content
        scredit = list(credit.split())
        scredit.remove(scredit[0])
        amnt = scredit.pop(0)
        user = (scredit)
        print(amnt)
        print(credit)
        print(user)
        amnts = int(amnt)
        username = str(user)
        print(username)
        file1 = open("@!" + (username) + ".txt", "a")
        file1.close
        file1 = open("@!" + (username) + ".txt", "r")
        cr = file1.read()
        cr = int(float(cr))
        total = (cr - amnts)
        #      if total<0:
        #        total=0
        file1.close
        file1 = open("@!" + (username) + ".txt", "w")
        total = str(total)
        file1.write(total)
        return person, credit
#check credits command
    if message.content.startswith('$checkcredits'):
        person = (message.author.id)
        usr = (message.author)
        usrnme = str(usr)
        await message.delete()
        prsntxt = str(person)
        file1 = open("@!['<@!" + (prsntxt) + ">']" + ".txt", "r")
        credits = file1.read()
        print(credits)
        await message.channel.send((usrnme) + (" has ") + (credits) +
                                   " Sociaw cwedits")
        print("code1")
    if message.content.startswith('$checkusr'):
        credit = message.content
        scredit = list(credit.split())
        scredit.remove(scredit[0])
        person = scredit.pop(0)
        usr = (message.author)
        usrnme = str(usr)
        await message.delete()
        prsntxt = str(person)
        file1 = open("@!['" + (prsntxt) + "']" + ".txt", "r")
        credits = file1.read()
        print(credits)
        await message.channel.send((person) + (" has ") + (credits) +
                                   " Sociaw cwedits")
        print("code12")
    if message.content.startswith('$help'):
        await message.channel.send(
            "```$help: awsk fow hewp \n$checkcredits: check cuwwent amount of sociaw cwedits.\n +credits/-credits: if uwu have pewmission +/- cwedits fwom specific usew\n (+/-credits xx mention user)\n $clear [Amount] if uwu have cleanup wowe cweaw x pwiow messages\n $checkusr @user checks others credits```"
        )
        print("code7")
    if message.content.startswith('I am'):
        person = (message.author)
        usern = str(person)
        file2 = open("Dadjokes.txt", 'a')
        joke = message.content
        file2.write(('"') + joke + ('"') + (' statement made by ') + usern +
                    ('\n'))
    if message.content.startswith("I'm"):
        person = (message.author)
        usern = str(person)
        file2 = open("Dadjokes.txt", 'a')
        joke = message.content
        file2.write(('"') + joke + ('"') + (' statement made by ') + usern +
                    ('\n'))
    if message.content.startswith('$getrolled'):
        msg = message.content
        await message.delete()
        await message.channel.send(
            'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    if message.content.startswith('$clear') and discord.utils.get(
            message.author.roles, name="Cleanup"):
        await message.delete()
        credit = message.content
        scredit = list(credit.split())
        scredit.remove(scredit[0])
        amnt = scredit.pop(0)
        amnts = int(amnt)
        await message.channel.purge(limit=amnts)
        print('Code 9')
    if message.content.startswith('leaderboard'):
        await message.delete()



#bot.run(os.getenv('TOKEN'))
client.run(os.getenv('TOKEN'))
