from platform import system


def get_os():
    a = system()
    if a == "Windows":
        return 1
    elif a == "Linux":
        return 2
    elif a == "Darwin":
        return 3
    else:
        return 4
