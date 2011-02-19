import bukkitmanager
import optparse
version = '0.1'
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

#begin by parsing command line arguments
#setup the fuckin parser
parser = optparse.OptionParser(\
 usage=bcolors.OKGREEN+"%prog"+bcolors.ENDC+" [options] [download | start | stop | restart | connect | deploy]",\
 description = 'Used to manage bukkit server. Relies on bukkitmanage.conf file for some settings.',\
 version=version)
parser.add_option('-v', '--verbose', action='store_true', help='print debug data')
(options, args) = parser.parse_args()
verbose("Args are: %s " % args)
if len(args) != 1:
    print bcolors.FAIL+"Error:"+bcolors.ENDC+" Please supply a command argument."
    parser.print_help()