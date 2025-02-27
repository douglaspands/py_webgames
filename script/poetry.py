import subprocess


def shell(cmd: str):
    return subprocess.run(cmd, shell=True, check=True, text=True)


def start():
    shell("flask run --host 0.0.0.0")


def debug():
    shell("flask run --debug --host 0.0.0.0")
