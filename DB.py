"""System Manager Discord Bot - DB Controler - V1.0
Created by: André G. Padovezi - Rusted Gear Softworks - 2024"""

import os.path
import sqlite3
from os import system, getcwd, path

pat = getcwd()
print('Tentando conexão ao banco de dados...')
if os.path.exists(f'{pat}/SQLite3.db'):
    conex = sqlite3.connect('SQLite3.db')
    print('Conectado.')
else:
    conex = sqlite3.connect('SQLite3.db')
    conex.cursor()
    print('Criando Tabelas, não encerre o programa!')
    conex.execute("CREATE TABLE DS_Servers(ds_id INTEGER NOT NULL, ds_name TEXT NOT NULL);")
    conex.execute("CREATE TABLE GAME_Servers(gs_name TEXT UNIQUE NOT NULL, gs_count TEXT UNIQUE NOT NULL, "
                  "gs_path TEXT NOT NULL, sv_id INTEGER NOT NULL, FOREIGN KEY(sv_id) REFERENCES DS_Servers (ds_id));")
    print('Concluído, DB pronto.')


def con():  # Execução inicial do arquivo
    print()


def select(query):  # Executa SELECT´s no Banco
    try:
        conex.cursor()
        return conex.execute(query).fetchall()
    except sqlite3.Error as e:
        print(f'Falha ao executar SELECT no DB:\n{e}')


def insert(query): # Executa query´s INSERT no banco
    try:
        conex.cursor()
        conex.execute(query)
        conex.commit()
        return 0
    except sqlite3.Error as e:
        print(f'Falha ao executar INSERT no DB:\n{e}')
        return 1
