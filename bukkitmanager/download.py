import urllib2
import optparse
import os.path
import sys

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
        print "Error: Only accept 1 argument. Please supply the version to download."
        parser.print_help()
        exit()
    try:
        download_number = int(args[0])
    except ValueError:
        print "Error: Must supply a numrical value for VERSION_NUMBER!"
        parser.print_help()
        exit()
    f = open("/".join(sys.path[0].split("/")[0:-1])+"/craftbukkit-%d.jar" % download_number, "w")
    f.write(urllib2.urlopen("http://bamboo.lukegb.com/browse/BUKKIT-CRAFTBUKKIT-%d/artifact/JOB1/CraftBukkit-JAR/craftbukkit-0.0.1-SNAPSHOT.jar" % download_number,None).read())
    f.close()

    
    
