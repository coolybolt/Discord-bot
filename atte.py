import discord
import os
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event



async def on_react(reaction,user):

#    if message.author == client.user:
#        person=(message.author)
#        return(person)
#    if reaction.emoji('❌'):
#      person=(message.author)
#      emoji = '\N{THUMBS UP SIGN}'
      await reaction.delete()
      await reaction.channel.send('hello!')
      print("code1")


client.run(os.getenv('TOKEN'))