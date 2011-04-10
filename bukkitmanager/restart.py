import optparse, stop, start, config
import pexpect

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
          
def restart(args):
    global options
    global screen_child
    #begin by parsing command line arguments
    #setup the fuckin parser
    parser = optparse.OptionParser(\
    usage=bcolors.OKGREEN+"%prog start"+bcolors.ENDC)
    parser.add_option('-v', '--verbose', action='store_true', help='print debug data')
    (options, args) = parser.parse_args(args)
    verbose("Args are: %s " % args)
    screen_child = pexpect.spawn("screen -S %s" % config.readScreenName())
    print bcolors.OKBLUE, "Restarting", bcolors.ENDC
    while True:
        try:
            screen_child.expect("no screen", timeout=3)
        except pexpect.TIMEOUT:
            stop.stop()
            ##SERVER STILL NEEDS RESTARTING HERE (FIRST CONFIG NEEDS TO BE ADVANCED TO STORE THE FILE NAME AND THE START PARAMS OF PREVIOUS START)
            break
        except pexpect.EOF, e:
            print bcolors.FAIL + "Process unexpectedly terminated\n%s" % e+bcolors.ENDC
            break
        start.start(config.readStartParams())