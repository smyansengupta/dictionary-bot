"""
Dictionary Bot
Created by Smyan Sengupta using Free Dictionary API
"""

import discord
import requests
import json
from discord.ext import commands

client = commands.Bot(command_prefix="d!", help_command=None)


@client.event
async def on_ready():
    print("Dictionary Bot is ready!")
    await client.change_presence(activity=discord.Game("d!help"))


@client.command()
async def help(ctx):
    h_info = discord.Embed(title="Help Menu", author="Dictionary Bot", description="All commands", color=discord.Color.blurple())
    h_info.add_field(name="d!define [word]", value="Gives definitions of the word", inline=False)
    h_info.add_field(name="d!help", value="Shows help menu", inline=False)

    await ctx.send(embed=h_info)


@client.command()
async def define(ctx, *, word):
    r = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    data = r.json()
    word = word.title()

    if data == {"title":"No Definitions Found","message":"Sorry pal, we couldn't find definitions for the word you were looking for.","resolution":"You can try the search again at later time or head to the web instead."}:
        error = discord.Embed(title="Error", color=discord.Color.blurple())
        error.add_field(name="Word not found", value="Please try again")
        await ctx.send(embed=error)
        return

    w_info = discord.Embed(title=word, color=discord.Color.blurple())
    for i in range(len(data[0]['meanings'])):
        w_info.add_field(name=data[0]['meanings'][i]['partOfSpeech'].title(), value=data[0]['meanings'][i]['definitions'][0]['definition'], inline=False)
    await ctx.send(embed=w_info)


# client.run("")
