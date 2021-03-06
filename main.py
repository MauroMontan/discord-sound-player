# This example requires the 'message_content' intent.
from discord import Client, Message, Intents
from bot.config import Config
from bot.audio_events import join, playSound, leave

class MyClient(Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: Message):
        print(f'Message from {message.author}: {message.content}')

        currentMessage:str = message.content
        args:list = currentMessage.split(" ")

        if message.content == "&join":
            await join(message)

        elif currentMessage.startswith("&play"):
            if len(args) == 2:
                currentAudio = args[1]
                await playSound(message,currentAudio)
            else:
                await message.channel.send("i just accept two args")
                return
        elif message.content == "&leave":
            await leave(message) 


intents = Intents.default()
intents.guild_messages = True


client = MyClient(intents=intents)
client.run(Config.TOKEN)
