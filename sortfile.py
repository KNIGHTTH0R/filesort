import os
import shutil

def makedir():
    '''create folder'''
    path = os.getcwd()
    directory = os.path.join(path, '{}' .format(dirname))
    
    if not os.path.exists(directory):
        return os.makedirs(directory)
    else:
        print('\nfolder already exist!')
        return main()

def searchfile():
    '''search specific file'''
    return

def movefile():
    '''move sorted file'''
    return

def main():
    '''main proccess'''
    global dirname
    dirname = input('\nInput new folder name: ')
    makedir()
    return

main()
