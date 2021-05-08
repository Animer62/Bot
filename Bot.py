import discord
import datetime

animes = []
times = []

client = discord.Client()

#@client.event
#async def on_ready(msg):
  #msg.channel.send("Welcome back!")


@client.event
async def yo(msg):
  if msg.author == client.user:
    return

  if msg.content == ('!yo'):
    await msg.channel.send('Yo guys wats up')

#command
@client.event
async def Hello(msg):
  if msg.author == client.user:
    return

  if msg.content.startswith('!hi'):
    await msg.channel.send('Hello from the other world~~~')
    
@client.event
async def add(msg):
  if msg.content == '!add':
    addAnime = await client.wait_for('Anime name?')
    animes.append(addAnime.content)
    addTime = await client.wait_for('Time?')
    times.append(addTime.content)
  
@client.event
async def view(msg):
  if msg.content == '!view':
    await msg.channel.send(animes)
    await msg.channel.send(times)
    

@client.event
async def remove(msg):
  if msg.content == '!remove':
    await msg.channel.send(animes)


client.run('ODM4ODU2NTA1OTUxMzg3NjY5.YJBMAA.l4K8miiiVbT0dMf0-6x7jm5gBa4')
