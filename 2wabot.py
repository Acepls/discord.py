import discord
from discord.ext import commands
import random
import json

from os import path

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='&')

with open("db.json") as dtb:
    db = json.load(dtb)

def update_db(database, filename):
    with open(filename, "w") as dtb:
        json.dump(database, dtb, indent=4)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="Kingdom Hearts 4"))

@bot.command()
async def quote(ctx):
    """Returns a random quote"""
    await ctx.send(random.choice(db["quotes"]))

@bot.command()
async def addquote(ctx, body: str, accredited: str):
    """Add a quote to the list of quotes"""
    quote_body = f"<{accredited}> {body}"
    if quote_body not in db["quotes"]:
        db["quotes"].append(quote_body)
        update_db(db, "db.json")
        await ctx.send('Quote added!')
    else:
        await ctx.send('Quote already exists, dummy!')

bot.run('NzI3NjY5MjkwMzQ5ODg3NTU2.XvwRVg.xCPLnP_bNdxi3sB81LwbhYj-8qE')
