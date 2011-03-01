import config
import os

def connect():
    os.system('screen -r %s' % config.readScreenName())
