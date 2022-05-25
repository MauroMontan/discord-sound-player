# This example requires the 'message_content' intent.
from re import split
from discord import Client, Message, Intents
from bot.config import Config
from bot.audio_events import join, playSound, leave

class MyClient(Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: Message):
        print(f'Message from {message.author}: {message.content}')

        splited = message.content
        print(type(splited))

        if message.content == "!join":
            await join(message)

        elif message.content == "!play":
            await playSound(message)


        elif message.content == "!leave":
            await leave(message) 


intents = Intents.default()
intents.guild_messages = True


client = MyClient(intents=intents)
client.run(Config.TOKEN)
