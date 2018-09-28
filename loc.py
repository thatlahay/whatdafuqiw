"""
How to bytes tell search
"""

#-> BOT DISCORD
import discord
import asyncio
import random
import requests
import json
import re
import random
from discord.ext.commands import Bot
from discord.ext import commands
from time import sleep

BOT_PREFIX = (",")
TOKEN_BOT = 'NDkxMjAzNzE2NDE4ODk1ODcy.DolDZQ.fdzXljtcxyRn5B2HeCjXTBry8vw'

client = discord.Client()

#-> BOT CONNECT

@client.event
async def on_ready():
	print("Bot is online !")
	await client.change_presence(game=discord.Game(name='client Bot'))

@client.event
async def on_message(message):
	woe_id = ""
	
	#What dafuq is this .
	bot_client_data = {"client_blame_1":"Thằng client nó lập trình tao ra chỉ để bắt tao làm hết công việc của nó. Thật khốn nạn.",
					  "client_blame_2":"client nó chơi dc"}
	
	#We dont want the bot send message to itself
	if message.author == client.user:
		return
	
	if message.content == "$chui help":
		await client.send_message(message.channel, "mày bấm $chui tên mod/admin")
		
	if message.content == "$chui client":	
		await client.send_message(message.channel, "Thằng Phate nó lập trình tao ra chỉ để bắt tao làm hết công việc của nó. Thật khốn nạn.")
		print("[Command] Hello client " + str(message.author) + str(message.channel))
	if message.content == "$chui datsausa":
		await client.send_message(message.channel, "Datsausa, nó từng gửi game hentai 9k cho client mà phải cày 1 đống mới ra được 1 cái hình đấy !! ")
		print("[Command] $chui datsausa")
	#Weather check
	if message.content.startswith("$check weather") and str(message.channel) == "check-thời-tiết":
		#-> add yahoo weather woeid here
		if re.search("hcm",message.content):
			woe_id = "1252431"
		if re.search("canduoc",message.content):
			woe_id = "1252350"
		if re.search("hanoi",message.content):
			woe_id = "1236594"
			
		#<- add yahoo weather woeid closed
		baseurl = "https://query.yahooapis.com/v1/public/yql?q="
		yql_query = 'select * from weather.forecast where woeid={0}'.format(woe_id) + "&format=json"
		yql_url = requests.get(baseurl+yql_query+"&format=json").json()
		
		
		F = int(yql_url['query']['results']['channel']['item']['condition']['temp'])
		
		#-> Print out what we got by the API
		await client.send_message(message.channel, "Ngày: " + yql_url['query']['results']['channel']['lastBuildDate'])
		await client.send_message(message.channel, yql_url['query']['results']['channel']['location']['city'])
		await client.send_message(message.channel, "Độ ẩm: " + yql_url['query']['results']['channel']['atmosphere']['humidity'])
		await client.send_message(message.channel, "Nhiệt độ: {0}".format(int((F - 32)/1.8000)) + " C") #This shit is change F to C
		await client.send_message(message.channel, "Mây: " + yql_url['query']['results']['channel']['item']['condition']['text'])
		#<- Print out what we got by the API
		
		
	#Delete 100 msg in a Channel
	if message.content.startswith("$clear"):
		msg = []
		number = 0
		async for x in client.logs_from(message.channel):
			msg.append(x)
			number += 1
		await client.delete_messages(msg)
		
		print("[DELETE] Deleted ",number, " in channel {0}".format(message.channel))
		
	if message.content.startswith("$test"):
		await client.send_message(message.channel, "<@{0}> XIN CHAO !!! TAO LA BOT PHATE VA TAO BIET TAG >:)".format(str(message.author.id)))
	if re.search(message.content,"<@491203716418895872>"):
		
		await client.send_message(message.channel, "<@{0}> Địt mẹ tag tao ăn lol ak. Lâu lâu mới dc cho online mà cũng bị làm phiền dkm.".format(str(message.author.id)))
	if message.content == "$show phate secret life":
		await client.send_message(message.channel,"just both dark and happy, it's a REAL CHAOS , no one can know what happend next.He's know who's he really are.The univers just like the chaos")

client.run(TOKEN_BOT)

#<- BOT DISCORD
