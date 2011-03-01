import config
import os

def connect(args):
    os.system('screen -r %s' % config.readScreenName())
