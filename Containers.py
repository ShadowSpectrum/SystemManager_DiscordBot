"""System Manager Discord Bot - Container Manager V1.2
Created by: André G. Padovezi - Rusted Gear Softworks - 2024"""

import os
import subprocess


def lists():
    fl = open("ps-a.txt", "w")
    fl.write(subprocess.check_output("docker ps -a", shell=True, text=True))
    return


"""def exe(name, func):
    try:
        # print(f'docker {func} {name}')
        a = subprocess.run(f"docker {func} {name}", shell=True, text=True, capture_output=True)
        return a
    except subprocess.CalledProcessError as e:
        # r = f'{e.returncode}: {e.output}'
        r = str()
        for c in e.stderr:

        return r"""


def exe(name, func):

    a = subprocess.run(f"docker {func} {name}", shell=True, text=True, check=False, capture_output=True)
    return a


def compose(func, path):
    a = str()
    if func == 'up':
        a = subprocess.run(f"cd {path[:len(path)-2]} && docker compose up -d --force-recreate", shell=True, text=True, check=False, capture_output=True)
    elif func == 'down':
        a = subprocess.run(f"cd {path[:len(path)-2]} && docker compose down", shell=True, text=True, check=False, capture_output=True)

    return a
