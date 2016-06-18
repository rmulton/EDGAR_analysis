# -*-coding:Latin-1 -*

'''
Module:     'unzip_files'
Aim:        Unzip all .zip files in a folder and its subfolders
Functions:  - unzip_file
            - unzip_everything
'''

################################################################################

import zipfile
import os.path

################################################################################

def unzip_file(path):

    '''
    Unzips the file for the given path
    path must be a string
    '''

    # opens the file
    file = open(path, 'rb')

    # creates the aim folder if not exist
    position = len(path) - 4
    directory_name = path[:position]
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    target_dir = directory_name + '/'

    #extracts all the files from the .zip directory
    z = zipfile.ZipFile(file)
    for name in z.namelist():
        outfile = open(target_dir + name, 'wb')
        outfile.write(z.read(name))
        outfile.close()
    file.close()

################################################################################

def unzip_everything():

    '''
    Unzips every .zip files contained in a folder and its subfolders
    '''

    # for every element in the directory
    for element in os.listdir():

        # if the element is a .zip file and hasn't been unziped, unzip it
        if os.path.isfile(element) and str(element[-4:]) == '.zip':

            if os.path.exists(element[:len(element)-4]):
                print(element, ' already unzipped')
            else:
                unzipFile(element)
                print(element, ' unzipped')

        #if the element is a folder unzips every .zip file in it
        elif not os.path.isfile(element):
            os.chdir(element)
            unzip_everything()
            os.chdir('..')

################################################################################
