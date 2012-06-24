#!/usr/bin/env python
import bukkitmanager
import optparse
version = '1.0'
possible_commands = ['download', 'start', 'stop', 'restart', 'connect', 'deploy','backup']

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
#setup the parser
parser = optparse.OptionParser(\
 usage=bcolors.OKGREEN+"%prog"+bcolors.ENDC+" [options] [download | start | stop | restart | connect | deploy]",\
 description = 'Used to manage bukkit server. Relies on bukkitmanage.conf file for some settings.',\
 version=version)
parser.disable_interspersed_args()
parser.add_option('-v', '--verbose', action='store_true', help='print debug data')
(options, args) = parser.parse_args()
verbose("Args are: %s " % args)
#check to make sure we have 1 argument or more
if len(args) < 1:
    print bcolors.FAIL+"Error:"+bcolors.ENDC+" Please supply a command argument."
    parser.print_help()
    exit()

verbose("Correct number of args supplied")
verbose("Config Options:\nusers:%s\nname:%s\ntesting:%s" % (bukkitmanager.config.users, bukkitmanager.config.name, bukkitmanager.config.test_server))
command = args[0]
if not command in possible_commands:
    print bcolors.FAIL+"Error:"+bcolors.ENDC+" Incorrect command argument."
    parser.print_help()
    exit()

getattr(getattr(bukkitmanager,command), command)(args[1:])