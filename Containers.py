"""System Manager Discord Bot - Container Manager V1.0
Created by: André G. Padovezi - Rusted Gear Softworks - 2024"""

import os
import subprocess


def lists():
    fl = open("ps-a.txt", "w")
    fl.write(subprocess.check_output("docker ps -a", shell=True, text=True))
    return


def exe(name, func):
    print('Here')
    print(f'docker {func} {name}')
    os.system(f"docker {func} {name}")


def compose(func, path):

    if func == 'up':
        os.system(f'cd {path} && docker compose up -d --force-recreate')
    elif func == 'down':
        os.system(f'cd {path} && docker compose down')
