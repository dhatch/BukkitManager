import urllib2
import optparse
import os.path
import sys

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
def download(args):
    global options
    parser = optparse.OptionParser(usage="%prog [options] VERSION_NUMBER")
    parser.add_option("-v", "--verbose", action = "store_true", help = "print debug data")
    (options, args) = parser.parse_args(args)
    verbose("Args are: %s " % args)
    if len(args) != 1:
        print bcolors.FAIL+"Error:"+ bcolors.ENDC + "Only accept 1 argument. Please supply the version to download."
        parser.print_help()
        exit()
    try:
        download_number = int(args[0])
    except ValueError:
        print bcolors.FAIL+"Error:"+bcolors.ENDC+"Must supply a numrical value for VERSION_NUMBER!"
        parser.print_help()
        exit()
    try:
        tested_url = urllib2.urlopen("http://ci.bukkit.org/job/dev-CraftBukkit/%d/artifact/target/craftbukkit-0.0.1-SNAPSHOT.jar" % download_number,None)  
    except urllib2.URLError as details:
        print bcolors.FAIL+"Error:"+bcolors.ENDC,details
        parser.print_help()
        exit()

    f = open(sys.path[0]+"/craftbukkit-%d.jar" % download_number, "w")
    f.write(tested_url.read())
    f.close()
    print bcolors.OKBLUE +"Download Complete" + bcolors.ENDC
