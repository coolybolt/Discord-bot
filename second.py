import discord
import os
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event



async def on_message(message):

    if message.author == client.user:
        person=(message.author)
        return(person)
    if message.content.startswith('$react'):
      person=(message.author)
      emoji = '\N{THUMBS UP SIGN}'
      await message.delete()
      await message.channel.send('hello!')
      print("code1")


client.run(os.getenv('TOKEN'))