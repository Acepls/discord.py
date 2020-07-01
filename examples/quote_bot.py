import discord
import json
import random

from os import path

description = '''The most bestest bot for 2wa purposes

Nut.'''
bot = commands.Bot(command_prefix='?', description=description)

with open("db.json") as dtb:
    db = json.load(dtb)

def update_db(database, filename):
    with open(filename, "w") as dtb:
        json.dump(database, dtb, indent=4)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!quote'):
            await message.channel.send(random(db["quotes"]).format(message))
        elif message.content.startswith('!addquote'):


client = MyClient()
client.run('NzI3NjY5MjkwMzQ5ODg3NTU2.XvvNeQ.QHJGj4ymoQSnAR_P2WwjKv0TUzw')
