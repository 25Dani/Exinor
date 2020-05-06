import discord

prefix = "ex-"
token = "NzA3MTgxNDM4MjY4NzM1NDk5.XrKJjw.DfdpP1sit8TiR3EhtUM1IZ1ZugE"

exinor = discord.Client()

@exinor.event
async def on_message(message):
    print(f"#{message.channel} : {message.content}")

    if message.content.find(f"{prefix}status") != -1:
        await message.channel.send("Exinor is running in **failsafe** mode due to **Technical Difficulties**")

exinor.run(token)