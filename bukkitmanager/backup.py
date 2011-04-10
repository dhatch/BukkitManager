import optparse
import shutil
import sys
import os
import datetime
import zipfile

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

#this is convenient
def zipper(dir, zip_file):
    zip = zipfile.ZipFile(zip_file, 'w', compression=zipfile.ZIP_DEFLATED)
    root_len = len(os.path.abspath(dir))
    for root, dirs, files in os.walk(dir):
    	#print root, dirs, files
        archive_root = os.path.abspath(root)[root_len:]
        for f in files:
            fullpath = os.path.join(root, f)
            archive_name = os.path.join(archive_root, f)
            print f
            zip.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
    zip.close()
    return zip_file
    
def backup(args):
	global options
	parser = optparse.OptionParser(usage="%prog [options] ")
	parser.add_option("-v", "--verbose", action = "store_true", help = "print debug data")
	(options, args) = parser.parse_args(args)
	verbose("Args are: %s " % args)
	## setting up the location for the world file to be saved to
	
	# split the list into strings
	location = sys.path[0].split("/")
	# create a seperate path for finding the world file
	world_location = "/".join(location)
	verbose("world folder in:"+world_location)
	# make the strings back into a list for location to save the backup world
	backup_location = os.path.join(world_location,"backups","world")
	# change the dir to find the world dir
	os.chdir(world_location)
	#find the current time
	today = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
	shutil.copytree("world", os.path.join(backup_location,today))
	#ZIP IT UP BITCH
	os.chdir(backup_location)
	#YEA MAN
	zipper(today,today+".zip")
	shutil.rmtree(today)
	print bcolors.OKGREEN + "Backup Done!" + bcolors.ENDC
if __name__ == "__main__":
	backup(sys.argv)
