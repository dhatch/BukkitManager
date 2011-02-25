import optparse
import os
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

def stop_server(args):
    global server_child
    server_child.sendline("stop")
    while True:
        try:
            server_child.expect(["[WARNING]|[SEVERE]", "Stopping server"], timeout = 5000)
        except pexpect.EOF:
            verbose("server successfully stopped")
            break
        except pexpect.TIMEOUT:
            server_child.close()
            break
    
        
def start(args):
    global options
    global server_child
    #begin by parsing command line arguments
    #setup the fuckin parser
    parser = optparse.OptionParser(\
     usage=bcolors.OKGREEN+"%prog start"+bcolors.ENDC+" [options] FILENAME [min_memory (MB)] [max_memory (MB)]")
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
    screen_child = pexpect.spawn("screen",["-m","-S",options.screen_name, "java","-Xms%dM" % min_memory,"-Xmx%dM" % max_memory,"-Xincgc","-jar",'%s' % file_n,"nogui"])
    verbose("process started")
    #begin processing the output from the screen session
    while True:
        try: 
            i = screen_child.expect(["[WARNING]", "[SEVERE]","[INFO]"])
        except pexpect.EOF, e:
            print bcolors.FAIL + "Process unexpectedly terminated\n%s" % e+bcolors.ENDC
            break
        except pexpect.TIMEOUT:
            pass
            verbose("Read timeout")
        verbose("Matched: %d, %s" % (i, screen_child.after))
        if i == 0:
            print bcolors.WARNING+screen_child.after+bcolors.ENDC
            if screen_child.after.find("FAILED TO BIND TO PORT") != -1:
                print bcolors.FAIL+"Cancelling start attempt...\nA server is already using the configured port. Perhaps try "+bcolors.OKBLUE\
                +"manage.py stop "+bcolors.ENDC+"or "+bcolors.OKBLUE+"manage.py restart"
                stop_server()
                break
        if i == 1:
            print bcolors.FAIL+screen_child.after+bcolors.ENDC
            print bcolors.FAIL+"Cancelling start attempt..."+bcolors.ENDC
            stop_server()
            break
        if i == 2:
            verbose(bcolors.OKBLUE+screen_child.after)
            if screen_child.after.find("Preparing level") != -1:
                print bcolors.OKGREEN+"Server starting... Please wait..."+bcolors.ENDC
            if screen_child.after.find("Done"):
                print bcolors.OKGREEN+"Server up and running. Setting up screen..."+bcolors.ENDC            
                #os.system("screen -r %s -X multiuser on" % options.screen_name)
                #add users to screen
                #eventually users to add should be read from config
                #users = ['dhatch', 'pconzone', 'beyring']
                #for u in users:
                #    os.system("screen -r %s -X acladd %s" % (options.screen_name, u))
                print bcolors.OKGREEN+"Started sucessfully with session name %s%s%s!" % (bcolors.OKBLUE, options.screen_name, bcolors.OKGREEN)+bcolors.ENDC\
                + "\nConnect with %smanage.py connect" % bcolors.OKBLUE+bcolors.ENDC
                #write screenname with pid out to bukkitmanger.conf
                screen_child.close(False) #close without killing screen
                break