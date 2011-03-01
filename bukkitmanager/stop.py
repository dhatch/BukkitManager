import optparse
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

def stop_server():
    global screen_child
    screen_child.sendline("stop")
    while True:
        try:
            screen_child.expect(["[WARNING]|[SEVERE]", "Exception"], timeout = 5000)
        except pexpect.EOF:
            verbose("server successfully stopped")
            screen_child.close()
            break
        except pexpect.TIMEOUT:
            screen_child.close()
            verbose("Force closed")
            break
        verbose("sent stop again")
        screen_child.sendline("stop")

def stop(args):
    