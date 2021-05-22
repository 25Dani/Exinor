import discord
from discord.ext import commands
from decouple import config
    
from datetime import datetime
import os

extdir = "extensions" 

prefix = ['x.', 'x. ', "X.", "X. "]
intents = discord.Intents.all()
client = commands.Bot(
    command_prefix=prefix, 
    intents=intents,
    case_insensitive=True
)

client.remove_command('help')

for filename in os.listdir(extdir):
    if filename.endswith(".py"):
        try: 
            extname = f"extensions.{filename[:-3]}"                            
            client.load_extension(extname)
            print(f" * '{extname}'  has been loaded")
        except Exception as e: print(e)
        
@client.event
async def on_ready():
    print(f'\n * Logged in as {client.user.name}#{client.user.discriminator} \n * Time: {datetime.now()}')
    
client.run(config("token"))