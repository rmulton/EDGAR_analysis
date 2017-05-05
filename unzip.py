import zipfile
import os.path

def unzip_file(path):
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

def unzip_everything(path):
    # for every element in the directory
    for element in os.listdir(path):
        # if the element is a .zip file and hasn't been unziped, unzip it
        filepath = path+'\\'+element
        if os.path.isfile(filepath) and filepath[-4:] == '.zip':
            if os.path.exists(filepath[:-4]):
                print('Already unzipped: ', element)
            else:
                print('Unzipping: ', element)
                unzip_file(filepath)
        #if the element is a folder unzips every .zip file in it
        elif not os.path.isfile(filepath):
            unzip_everything(filepath)