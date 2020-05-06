import discord

# token is stored in a seperate file in the same folder called token.txt
# if u r using this code please create said text file put your token there
# this is done for improved security reasons
def read_token():
    with open ("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

version = "Exinor Beta 0.2"
build = "Nightly"
prefix = "e-"

client = discord.Client()

@client.event
async def on_message(message):                  
    guildID = client.get_guild(707173698418769920)

    print("Message sent: " + message.content)
    if message.content.find(f"{prefix}") != -1:
        await message.channel.send("hello")
   
    elif message.content.find(f"{prefix}members") != -1:
        await message.channel.send(f"No. of members in this : {guildID.member_count}")

    elif message.content.find(f"{prefix}channel") != -1:
        await message.channel.send(f"Name of this channel: {message.channel}")

client.run(token)