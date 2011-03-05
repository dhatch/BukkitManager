import config
import os, sys, optparse

def verbose(string):
    global options
    if options.verbose: print string

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
        
def deploy(args):
    global options
    global screen_child
    #begin by parsing command line arguments
    #setup the fuckin parser
    parser = optparse.OptionParser(\
        usage=bcolors.OKGREEN+"%prog start" + bcolors.ENDC)
    parser.add_option('-v', '--verbose', action='store_true', help='print debug data')
    parser.add_option('--commit-message', help='set commit message')
    parser.add_option('-n', '--no-commit', help='don\' commit after the deploy')
    (options, args) = parser.parse_args(args)
    if config.test_server:
        print bcolors.FAIL, "Must be used in a test directory.", bcolors.ENDC
        sys.exit()
    