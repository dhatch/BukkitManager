import optparse
import subprocess

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

def start(args):
    global options
    #begin by parsing command line arguments
    #setup the fuckin parser
    parser = optparse.OptionParser(\
     usage=bcolors.OKGREEN+"%prog"+bcolors.ENDC+" [options] FILENAME [min_memory (MB)] [max_memory (MB)]")
    parser.add_option('-v', '--verbose', action='store_true', help='print debug data')
    #later replace default value here with config
    parser.add_option('-s', '--screen-name', action='store', help='the name of the screen session', default='minecraft-tester')
    (options, args) = parser.parse_args(args)
    verbose("Args are: %s " % args)
    if len(args) < 1:
        print bcolors.FAIL+"Error:"+bcolors.ENDC+" Please supply a command argument."
        parser.print_help()
        exit()
    ##READY TO START SERVER
    #defaults here should depend on config, eventually add in setting based on input
    min_memory = 512
    max_memory = 512
    file_n = args[0]
    verbose(bcolors.OKGREEN+"Running:"+bcolors.ENDC+" screen -mdS %s java -Xms%dM -Xmx%dM -Xincgc -jar %s nogui" % (options.screen_name, min_memory, max_memory, file_n))
    subprocess.Popen("/usr/bin/screen -mdS %s java -Xms%d -Xmx%d -Xincgc -jar %s nogui" % (options.screen_name, min_memory, max_memory, file_n))
    subprocess.Popen("/usr/bin/screen -Xr %s multiuser on" % options.screen_name, stdout=subprocess.STDOUT)
    subprocess.Popen("/usr/bin/screen -Xr minecraft/%s acladd dhatch" % options.screen_name, stdout=subprocess.STDOUT)
    