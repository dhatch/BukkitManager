import optparse
import pexpect
import config
import sys

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

def stop_server():
    global screen_child
    screen_child.sendline("stop")
    stop_attempts = 1
    while True:
        try:
            screen_child.expect(["\[WARNING\]","\[SEVERE\]", "Exception"], timeout = 5)
        except pexpect.EOF:
            verbose("server successfully stopped")
            print bcolors.OKGREEN + 'Server stopped' + bcolors.ENDC
            screen_child.close()
            break
        except pexpect.TIMEOUT:
            if stop_attempts > 4:
                screen_child.close()
                print bcolors.WARNING + 'Server force closed' + bcolors.ENDC
                verbose("Force closed")
                break
        verbose("sent stop again")
        screen_child.sendline("stop")
        stop_attempts += 1

def stop(args):
    global options
    global screen_child
    #begin by parsing command line arguments
    #setup the fuckin parser
    parser = optparse.OptionParser(\
        usage=bcolors.OKGREEN+"%prog start" + bcolors.ENDC)
    parser.add_option('-v', '--verbose', action='store_true', help='print debug data')
    (options, args) = parser.parse_args(args)
    verbose("Attempting to stop "+config.readScreenName())
    screen_child = pexpect.spawn('screen', ['-r', config.readScreenName()])
    try:
        screen_child.expect('There is no screen', timeout = 1)
        print bcolors.FAIL + 'Server not found to be running... try %smanage.py start%s' % (bcolors.OKBLUE, bcolors.ENDC)
    except pexpect.TIMEOUT:
        stop_server()