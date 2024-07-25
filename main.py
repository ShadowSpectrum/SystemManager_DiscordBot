"""System Manager Discord Bot V1.2
Created by: André G. Padovezi - Rusted Gear Softworks - 2024"""

import discord
import Containers
from discord.ext import commands
import DB

description = '''Gerenciador de Game Servers'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='=', description=description, intents=intents)


def tra(b):  # Recebe o resultado de um SELECT, 2 tuplas, e devolve uma string tratada
    a = str('')
    for c in b:
        for i in c:
            a = a + i.strip() + '\n'
    return a


@bot.event
async def on_ready():  # Inicialização do Bot
    DB.con()
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def helps(ctx):  # exibe a tela de ajuda
    """Adds two numbers together."""
    await ctx.send('Ajuda:')
    await ctx.send()


@bot.command()
async def ds_cad(ctx, nome):  # Cadastro de DS_Servers
    guild_id = ctx.guild.id
    query = f'INSERT INTO DS_servers VALUES("{guild_id}", "{nome}");'
    ex = DB.insert(query)
    if ex == 0:
        await ctx.send('Cadastro Realizado com sucesso')
    else:
        await ctx.send(f'Processo finalizado com erro, consulte o console para mais detalhes.')


@bot.command()
async def gs_cad(ctx, name, path, cnt_name):  # Cadastro de Game_Servers
    """=gs_cad Teste /opt/Apps/Teste teste_dockerapi"""
    guid_id = ctx.guild.id
    query = f'INSERT INTO GAME_SERVERS (gs_name, gs_count, gs_path, sv_id)' \
            f'VALUES("{name}", "{cnt_name}", "{path}", "{guid_id}");'
    ex = DB.insert(query)
    if ex == 0:
        await ctx.send('Cadastro realizado com sucesso')
    else:
        await ctx.send('Processo finalizado com erro, consulte o console para mais detalhes.')


@bot.command()
async def cont_lst(ctx):  # lista os containers do docker
    Containers.lists()
    await ctx.send(file=discord.File('ps-a.txt'))


@bot.command()
async def lst(ctx):  #Lista os Game_Servers do DS_Server:
    guid_id = ctx.guild.id
    b = DB.select(f"SELECT gs_name FROM GAME_Servers WHERE sv_id='{guid_id}'")
    a = 'Game_Servers Cadastrados:\n' + tra(b)
    await ctx.send(a)


@bot.command()
async def gsv(ctx, fun, name):  # Controle de Game_Servers
    try:
        con_name = tra(DB.select(f"SELECT gs_count FROM GAME_Servers WHERE gs_name = '{name}'"))
        path = tra(DB.select(f"SELECT gs_path FROM GAME_Servers WHERE gs_name = '{name}'"))
        # print(con_name, '', path)
        a = str()
        if fun in 'start':
            a = Containers.exe(con_name, 'start')
            print()
        elif fun == 'stop':
            a = Containers.exe(con_name, 'stop')
            print()
        elif fun == 'restart':
            a = Containers.exe(con_name, 'restart')
            print()
        elif fun == 'teardown':
            a = Containers.compose('down', path)
            print()
        elif fun == 'recreate':
            a = Containers.compose('up', path)
            print()
        else:
            a = '-'
        if a.returncode != 0:
            await ctx.send(f'Erro ao executar função:\nCódigo: {a.returncode}\nDescrição:{a.stderr}')
        else:
            await ctx.send('Comando executado com sucesso.')

    except ReferenceError as e:
        print('Erro de Syntaxe: gsv start|stop|restart|teardown|recreate GAME_SERVER_NAME')
        print(e)


bot.run('BOT_TOKEN')
