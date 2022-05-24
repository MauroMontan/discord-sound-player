# This example requires the 'message_content' intent.

import discord


import discord
from bot.config import Config


async def voiceConnectionsHandler(message: discord.Message):

    if message.content == "!join":
        if message.author.voice is None:
            await message.channel.send("You are not connected to a voice channel.")
            return
        #Connect to voice channel
        await message.author.voice.channel.connect()
        await message.channel.send("Connected.")

    elif message.content == "!leave":
        if message.author.voice is None:
            await message.channel.send("Not connected.")
            return

        #Disconnect
        await message.guild.voice_client.disconnect()
        await message.channel.send("I disconnected.")




class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message:discord.Message):
        print(f'Message from {message.author}: {message.content}')
        await voiceConnectionsHandler(message)

intents = discord.Intents.default()
intents.guild_messages = True


client = MyClient(intents=intents)
client.run(Config.TOKEN)





