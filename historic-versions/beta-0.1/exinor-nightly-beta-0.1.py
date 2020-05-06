import discord

# token is stored in a seperate file in the same folder called token.txt
# if u r using this code please create said text file put your token there
# this is done for improved security reasons
def read_token():
    with open ("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()

async def on_message(message):                   
    guildID = client.get_guild(000000000000000000) # replace zeros with your guild ID

    print("Message sent: " + message.content)
    if message.content.find("e;hi") != -1:
        await message.channel.send("hello \n howdy")

    elif message.content.find("e;members") != -1:
        await message.channel.send(f"No. of members in this : {guildID.member_count}")

    elif message.content.find("e;channel") != -1:
        await message.channel.send(f"Name of this channel: {message.channel}")

client.run(token)