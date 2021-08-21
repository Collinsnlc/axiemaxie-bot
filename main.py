import discord

import os

import requests
import json

from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

api_requests = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false')
api = json.loads(api_requests.content)


#url = "https://www.coingecko.com/en/coins/smooth-love-potion"
#page = requests.get(url)
#soup = BeautifulSoup(url, 'lxml')

#item = soup.find('a',class_="").text
#itemprice = soup.find('span',class_='pi__price').text
#iii = str(itemprice)



@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('!hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('!akuma'):
    await message.channel.send('Akuma is looking for a bebe')

  if message.content.startswith('!btc'):
    await message.channel.send(api[0]['current_price'])

  if message.content.startswith('!eth'):
    await message.channel.send(api[1]['current_price'])

  if message.content.startswith('!paege'):
    await message.channel.send("Paege is a vampire!")

  if message.content.startswith('!allen'):
    await message.channel.send("She is an ALIENNNNN")

  if message.content.startswith('!migs'):
    await message.channel.send("Bow down to our master Miguel")

  if message.content.startswith('!squid'):
    await message.channel.send("He stayed up too late he is sleeping still")

  if message.content.startswith('!raccoon'):
    await message.channel.send("this is the vampire lord up all night and sleeping all day")

  

  






client.run('ODc4NDMzMTMwMjcxMzcxMjc0.YSBGmg.S1vGjNM1Ni4FX7Cz4nWfUmfku_E')
  
