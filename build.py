import os

home = os.getcwd()
for fileName in os.listdir(home) :
    if os.path.isdir(fileName) and not fileName.startswith('.') :
        path = home + os.path.sep + fileName
        file = open(path + '.link', 'w+')
        file.write('path=' + path)
        file.close()
