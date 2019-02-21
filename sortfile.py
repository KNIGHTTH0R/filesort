import os
import shutil

def makedir():
    '''create folder'''
    global path
    path = os.getcwd()
    directory = os.path.join(path, '{}' .format(dirname))
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        return searchfile()
    else:
        print('\nfolder already exist!')
        return main()

def searchfile():
    '''search specific file'''
    global filename

    filename = []
    olpath = path + '/' + oldir

    for f in os.listdir(olpath):
        if os.path.isfile(os.path.join(olpath, f)):
            filename.append(f)

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
    oldir = input('\nInput source folder: ')
    dirname = input('\nInput new folder name: ')

    return makedir()

main()
