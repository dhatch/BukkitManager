import sys, os.path

#name
name = sys.path[0].split("/")[-1]
#set testing server
if name.find('test_') == 0:
    test_server = True
else:
    test_server = False
    
#users
users = list()
try:
    ops_file = open(os.path.join(sys.path[0],'ops.txt'), 'r')
    for line in ops_file:
        users += line
    ops_file.close()
except IOError:
    #default fall through
    users = ['dhatch','pconzone','beyring']

CONFIG_FILE_NAME = '.bukkitmanager.conf'
def getConfigHandle(mode = 'r'):
    return open(os.path.join(sys.path[0],CONFIG_FILE_NAME), mode)
    
def writeScreenName(name):
    fh = getConfigHandle('w+')
    fh.write(name)
    fh.close()
    
def readScreenName():
    fh = getConfigHandle()
    name = fh.readline()
    fh.close()
    return name