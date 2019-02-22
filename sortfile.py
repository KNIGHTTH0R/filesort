import os
import shutil

def makedir():
    '''create folder'''
    global path
    path = os.getcwd()
    directory = os.path.join(path, dirname)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        return searchfile()
    else:
        print('\nfolder already exist!')
        return main()

def searchfile():
    '''search specific file'''
    global filename
    global dirpath
    
    filename = []
    dirpath = ''
    #find through entire folder
    def findsubdir(parent, subdir):
        
        newpath = os.path.join(parent, subdir)
        dirpath = os.path.join(dirpath, subdir)

        for f in os.listdir(newpath):
            if findby == '1':
                if os.path.isfile(os.path.join(newpath, f)):
                    if filepart in f:
                        filename.append(f)
                else:
                    findsubdir(newpath, f)
            else:
                if os.path.isfile(os.path.join(newpath, f)):
                    if '.txt' in f:
                        with open(os.path.join(dirpath, f)) as file:
                            contents = file.read()
                            if filepart in contents:
                                filename.append(f)
                else:
                    findsubdir(newpath, f)

    findsubdir(path, oldir)

    return movefile()

def movefile():
    '''move sorted file'''

    for i in filename:
        dir_from = path + '/' + oldir + '/' + i
        dir_to = path + '/' + dirname + '/' + i
        shutil.move(dir_from, dir_to)
    
    return

def main():
    '''main proccess'''
    
    global dirname
    global oldir
    global filepart
    global findby
    findby = input('\nSelect the method:\n[1] find by file name\n[2] find by file content\n>> ')
    if findby != ('1' and '2'):
        print('\nPlease input 1 or 2 only!')
        return main()

    oldir = input('\nInput source folder: ')
    dirname = input('\nInput new folder name to create: ')
    filepart = input('\nInput keyword: ')
    return makedir()

main()
