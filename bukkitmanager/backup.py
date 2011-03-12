import optparse
from datetime import *
import sys
import os.path

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def verbose(string):    
    global options
    if options.verbose: print string

def backup(args):
    global options
    parser = optparse.OptionParser(usage="%prog [options] ")
    parser.add_option("-v", "--verbose", action = "store_true", help = "print debug data")
    parser.add_option("-f", "--file-list", help = "Enter a list of additional files you want to backup.")
    parser.add_option("-l", "--location", help = "Enter a directory to save the file(s) to.")
    (options, args) = parser.parse_args(args)
    verbose("Args are: %s " % args)
