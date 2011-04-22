import sys, os.path

#name
name = sys.path[0].split("/")[-1]
test_server = None
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
        users.append(line.strip())
    ops_file.close()
except IOError:
    #default fall through
    users = ['dhatch','pconzone','beyring','minecraft']

CONFIG_FILE_NAME = '.bukkitmanager.conf'
def getConfigHandle(mode = 'r'):
    return open(os.path.join(sys.path[0],CONFIG_FILE_NAME), mode)
    
def writeScreenName(name):
    name += "\n"
    fh = getConfigHandle()
    contents = fh.readlines()
    if len(contents) < 1: 
        contents.append(name)
    else:
        contents[0] = name
    fh.close()
    fh = getConfigHandle("w+")
    fh.writelines(contents)      
    fh.close()
    
def readScreenName():
    fh = getConfigHandle()
    name = fh.readline().strip()
    fh.close()
    return name
    
def writeStartParams(params):
    fh = getConfigHandle()
    contents = fh.readlines()
    if len(contents) < 2:
        if len(contents) == 1:
            contents.append("@".join(params))
        else:
            contents.append("temp")
            contents.append("@".join(params))
    else:
        contents[1] = "@".join(params)
    fh.close()
    fh = getConfigHandle("w+")
    fh.writelines(contents)
    fh.close()
    
def readStartParams():
    fh = getConfigHandle()
    params = fh.readlines()[1].split("@")
    fh.close()
    return params