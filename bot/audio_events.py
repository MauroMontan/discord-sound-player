from discord import Message, FFmpegPCMAudio


async def join(message: Message):
    if message.author.voice is None:
        await message.channel.send("You are not connected to a voice channel.")
        return
        #Connect to voice channel
    await message.author.voice.channel.connect()
    await message.channel.send("Connected.")


async def leave(message: Message):
    if message.author.voice is None:
        await message.channel.send("Not connected.")
    
        #Disconnect
    await message.guild.voice_client.disconnect()
    await message.channel.send("I disconnected.")


async def playSound(message: Message,currentTrack:str):
    if message.guild.voice_client is None:
        return
    
    try:
        print(currentTrack)
        message.guild.voice_client.play(FFmpegPCMAudio(f"./sounds/{currentTrack}.mp3"))
   
    except:
        await message.channel.send("no sé que tratas de decir.")
