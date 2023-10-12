import os
import requests
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
my_secret = os.environ['env']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def getJoke():
    r = requests.get("https://v2.jokeapi.dev/joke/Programming") #https://v2.jokeapi.dev/joke/Any for any joke
    return r.json()

@client.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("hey dirtbag")

@client.event
async def on_message(message):
    if message.content == 'tell me a joke':
      joke = getJoke()
      if joke['type'] == 'twopart':
        await message.channel.send(joke['setup'])
        await message.channel.send(joke['delivery'])
      else:
        await message.channel.send(joke['joke'])
  
client.run(my_secret)
