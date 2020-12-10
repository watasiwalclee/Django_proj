from discord.ext import commands
from discord import Embed, Game
import sqlite3

client = commands.Bot(command_prefix='#')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=Game('呀哈囉 $uehelp'))

@client.event
async def on_message(message):
    print(message.guild,message.channel,message.author.display_name,message.content,sep='   ')
    await client.process_commands(message)


client.run('NjkwNzYyNzMyOTIzOTEyMzMz.XnWI7Q.snFBjozJTeTTcxAC446VL-Lsjbg')