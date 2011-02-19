import urllib2
import optparse
def verbose(string):    
    global options
    if options.verbose: print string
def download(args):
    parser = optparser.OptionParser()
    parser.add_option("-v", "--verbose", action = "store_true", help = "print debug data")
    (options, args) = parser.parse_args()
    verbose("Args are: %s " % args)
    
    url = urllib2.urlopen("http://bamboo.lukegb.com/browse/BUKKIT-CRAFTBUKKIT/",None)
    
    
