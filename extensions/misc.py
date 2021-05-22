import discord
from discord import Embed, Color
from discord.ext import commands

import json

data = json.load(open('data.json', 'r'))

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['inv'])
    async def invite(self, ctx):
        invite_link = data["invite"]
        
        embed = Embed(
            title = 'Invite Exinor',
            description = f'**[Click Here!]({invite_link} "Invite Exinor")**', 
            color = Color.darker_gray()
        )

        embed.set_thumbnail(url = self.client.user.avatar_url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Misc(client))
