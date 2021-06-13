import discord
import os
import random
import quotes_collection
import emoji

# get the discord client working
client = discord.Client()

# method to extract Shayari / Poetry
def quote():

  # my chosen way of getting the Shayaris was
  # storing them in a dictionary in the file quotes_collection.py

  dict_key = random.choice(list(quotes_collection.q))
  msg = quotes_collection.q[dict_key][random.randint(0, len(quotes_collection.q[dict_key]))] + '\n\n' + dict_key
  return msg


# Logging in as Shayari Bot Alert
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


# read messages and give necessary outputs
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  # store message in a variable
  msg = message.content

  # if the message has -irshaad then write Shayari
  if message.content.startswith('-irshaad'):
    shayari = quote()
    await message.channel.send(shayari)

  # if the message has waah waah anywhere then send the clapping emoji
  if 'waah waah' in str(message.content):
    await message.channel.send(emoji.emojize(':clap:'))

  # if the message only has '-arz kiya hai' then write irshaad
  if message.content.startswith('-arz kiya hai') and    len(msg.split('-arz kiya hai',)[1]) == 0:
    await message.channel.send('irshaad')

  # if the message has '-arz kiya hai' followed by Shayari then give a random compliment
  elif message.content.startswith('-arz kiya hai') and    len(msg.split('-arz kiya hai ',)[1]) > 0:

    # randomised compliments
    compliments = ['itni gahrai', 'oho itna showoff', 'phoda','waah waah', 'what a charmer']
    await message.channel.send(random.choice(compliments))


client.run(os.environ['TOKEN'])
