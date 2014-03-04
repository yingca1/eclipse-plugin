import os

list = os.listdir(os.getcwd())
for fileName in list :
    if os.path.isdir(fileName) and not fileName.startswith('.') :
        path = os.getcwd() + os.path.sep + fileName
        file = open(path + '.link', 'w+')
        file.write('path=' + path)
        file.close()
