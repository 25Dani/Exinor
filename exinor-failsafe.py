import discord

# token is stored in a seperate file in the same folder called token.txt
# if u r using this code please create said text file put your token there
# this is done for improved security reasons
def read_token():
    with open ("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

prefix = "ex-"

exinor = discord.Client()

@exinor.event
async def on_message(message):
    print(f"#{message.channel} : {message.content}")

    if message.content.find(f"{prefix}status") != -1:
        await message.channel.send("Exinor is running in **failsafe** mode due to **Technical Difficulties**")

exinor.run(token)