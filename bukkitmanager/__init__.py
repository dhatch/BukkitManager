import connect
import deploy
import download
import restart
import start
import stop
import sys, os.path

#name
name = sys.path[0].split("/")[-1]
#set testing server
if name.find('test_') != -1:
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

