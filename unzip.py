import zipfile
import os

def unzip_file(filepath):
    file = open(filepath, 'rb')
    z = zipfile.ZipFile(file)
    path = os.path.split(filepath)
    target_dir = os.path.join(path[0], path[1][:-4])

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    for filename in z.namelist():
        target_file = os.path.join(target_dir, filename)
        outfile = open(target_file, 'wb')
        outfile.write(z.read(filename))
        outfile.close()
    file.close()

def unzip_everything(target_dir):
    for filepath in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filepath)
        if filepath[-4:]=='.zip':
            if os.path.exists(filepath[:-4]):
                print('{} already unzipped'.format(filepath))
            else:
                print('Unzipping {}'.format(filepath))
                unzip_file(filepath)

