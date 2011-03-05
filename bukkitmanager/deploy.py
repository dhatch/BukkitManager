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
    (options, args) = parser.parse_args(args)
    if not config.test_server:
        print bcolors.FAIL, "Must be used in a test directory.", bcolors.ENDC
        sys.exit()
    else:
        print bcolors.OKGREEN, "Deploying",bcolors.ENDC
        r = os.system("git checkout master")
        if r == 0:
            r = os.system("git push file://%s master" % os.path.join("/".join(sys.path[0].split("/")[0:-1]), config.name[5:]))
        if r == 0:
            print bcolors.OKGREEN, "Deployed", bcolors.ENDC
        else:
            print bcolors.FAIL, "Error", bcolors.ENDC