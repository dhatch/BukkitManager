import optparse
import os
import subprocess, select

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
    parser.add_option('-s', '--screen-name', action='store', help='the name of the screen session', default='minecraft_tester')
    (options, args) = parser.parse_args(args)
    verbose("Args are: %s " % args)
    if len(args) < 1:
        print bcolors.FAIL+"Error:"+bcolors.ENDC+" Please supply a command argument."
        parser.print_help()
        exit()
    ##READY TO START SERVER
    #defaults here should depend on config, eventually add in setting based on input
    try:
        min_memory = args[1]
    except IndexError:
        min_memory = 512
    try:
        max_memory = args[2]
    except IndexError:
        max_memory = 512
    file_n = args[0]
    verbose(bcolors.OKGREEN+"Running:"+bcolors.ENDC+" screen -mS %s java -Xms%dM -Xmx%dM -Xincgc -jar %s nogui" % (options.screen_name, min_memory, max_memory, file_n))
    screen_start = subprocess.Popen((["screen", "-m","-S",options.screen_name, "java -Xms%dM -Xmx%dM -Xincgc -jar %s nogui" % (min_memory, max_memory, file_n)]),
    stdout=subprocess.PIPE,\
    stdin=subprocess.PIPE)

    verbose("process started")
    #begin processing the output from the screen session
    stopping = False
    poll = select.poll()
    poll.register(screen_start.stdout, select.POLLIN)
    while True:
        #read lines
        line = None
        if poll.poll():
            line = screen_start.stdout.readline()
        verbose("Line: %s" % line)
        if line.find("[WARNING]") != -1:
            print bcolors.WARNING+line
            if line == '**** FAILED TO BIND TO PORT!':
                print bcolors.FAIL+"Cancelling start attempt...\nA server is already using the configured port. Perhaps try manage.py stop"
                screen_start.communicate("stop\n")
                stopping = True
            
        if line.find("[SEVERE]") != -1:
            print bcolors.FAIL+line
            print bcolors.FAIL+"Cancelling start attempt..."
            screen_start.communicate("stop\n")
            stopping = True
        if line.find("Preparing level") != -1:
            print bcolors.OKBLUE+"Server starting... Please wait..."
        if line.find("Done") != -1:
            print bcolors.OKGREEN+"Server up and running. Setting up screen..."
        
        
             
    #os.system("screen -r %s -X multiuser on" % options.screen_name)
    #add users to screen
    #eventually users to add should be read from config
    #users = ['dhatch', 'pconzone', 'beyring']
    #for u in users:
    #    os.system("screen -r %s -X acladd %s" % (options.screen_name, u))
    print bcolors.OKGREEN+"Started sucessfully with session name %s%s%s!" % (bcolors.OKBLUE, options.screen_name, bcolors.OKGREEN)+bcolors.ENDC\
    + "\nConnect with %s manage.py connect" % bcolors.OKBLUE
    #write screenname with pid out to bukkitmanger.conf