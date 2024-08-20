"""System Manager Discord Bot V2.0
Created by: André G. Padovezi - Rusted Gear Softworks - 2024"""

import discord
import Containers
from discord.ext import commands
import DB
from OS import get_os

description = '''Gerenciador de Game Servers'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='=', description=description, intents=intents)

SO = get_os()


def tra(b):
    """""Trata o resultado de um select
        :return - sring"""""
    a = str('')
    for c in b:
        for i in c:
            a = a + i.strip() + '\n'
    return a


@bot.event
async def on_ready():
    """"Inicialização do Bot"""
    DB.con()
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


bot.run('BOT_TOKEN')
