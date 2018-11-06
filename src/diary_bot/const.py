import os


def TOKEN():
    return os.environ['TOKEN_TELEGRAM']


def INTENT_START():
    return [
        "Hi, I'm Diary Bot, your personal diary. Nice to meet you. :)"
    ]
