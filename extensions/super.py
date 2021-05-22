import discord
from discord.ext import commands

import os
import json

data = json.load(open('data.json', 'r'))     

class Super(commands.Cog):

    def __init__(self, client):
        self.client = client
                
    # Discord command to load Extensions
    @commands.command(aliases=['ld'])
    async def load(self, ctx, extension:str):
        if ctx.author.id in data['superids']:
            try:
                if extension == 'all':
                    for filename in os.listdir("extensions"):
                        if filename.endswith(".py"):
                            try: 
                                extname = f"extensions.{filename[:-3]}"                            
                                self.client.load_extension(extname)
                                print(f" * '{extname}'  has been loaded")

                            except Exception as e: print(e) 

                    await ctx.send('`All Extensions have been loaded!`') 

                else: 
                    self.client.load_extension(f'extensions.{extension}')
                    await ctx.send('`The extension has been loaded!`')
                
            except:
                await ctx.send('`Please provide the extension to load!`')
        
        else: await ctx.send('`Only the devs can use this command!`')


    # Discord command to unload Extensions
    @commands.command(aliases=['uld'])
    async def unload(self, ctx, extension:str):
        if ctx.author.id in data['superids']:
            try:
                if extension == 'all':
                    for filename in os.listdir("extensions"):
                        if filename.endswith(".py"):
                            try: 
                                extname = f"extensions.{filename[:-3]}" 

                                if extname != 'extensions.super':                      
                                    self.client.unload_extension(extname)
                                    print(f" * '{extname}'  has been unloaded")     

                                else: ctx.send('`You can\'t unload that!`')

                            except Exception as e: print(e)
    
                    await ctx.send('`All Extensions have been unloaded!`') 
     
                else:
                    if extension != 'super':  
                        self.client.unload_extension(f'extensions.{extension}')
                        await ctx.send('`The extension has been unloaded!`')

                    else:
                        await ctx.send('`You can\'t unload that!`')

            except:
                await ctx.send('`Please provide the extension to unload!`')
        
        else: await ctx.send('`Only the devs can use this command!`')


    # Discord command to reload Extensions
    @commands.command(aliases=['rld'])
    async def reload(self, ctx, extension:str):
        if ctx.author.id in data['superids']:
            try: 
                if extension == 'all':
                    for filename in os.listdir("extensions"):
                        if filename.endswith(".py"):
                            try: 
                                extname = f"extensions.{filename[:-3]}" 

                                if extname != 'extensions.super':                      
                                    self.client.reload_extension(extname)
                                    print(f" * '{extname}'  has been reloaded")     

                                else: ctx.send('`You can\'t reload that!`')

                            except Exception as e: print(e)
    
                    await ctx.send('`All Extensions have been reloaded!`')

                else: 
                    if extension != 'super':
                        self.client.reload_extension(f'extensions.{extension}')
                        await ctx.send('`The extension has been reloaded!`')

                    else:
                        await ctx.send('`You can\'t unload that!`')

            except Exception as e:
                await ctx.send('`Please provide the extension to reload!`')
                print(e)
        
        else: await ctx.send('`Only the devs can use this command!`')


def setup(client):
    client.add_cog(Super(client))
