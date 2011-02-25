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

args = "Null"
parser.add_option("-v", "--verbose", action = "store_true", help = "print debug data")
(options, args) = parser.parse_args(args)
verbose("Args are: %s " % args)
parser.add_option("-f", "--file-list", action = "store_true", help = "Enter a list of files you want to backup.")
(options, args) = parser.parse_args(args)
filelist("Args are %s " % args)
parser.add_option("-l", "--location", action = "store_true", help = "Enter a directory to save the file(s) to.")
(options, args) = parser.parse_args(args)
location("Args are %s " % args)
parser.add_option("-n", "--name", action = "store_true", help = "Enter the name of the file to save as.")

