import os
import urllib.request
from urllib.error import *
from socket import timeout
from http.client import IncompleteRead

def download_edgar(periods, target_dir):

    # Create year directory if not existing
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print('Created target directory {}'.format(target_dir))
    else:
        print('Target directory {} already exists'.format(target_dir))

    print('Downloading from year {} quarter {}, to year {} quarter {}...'.format(periods[0]['year'], periods[0]['quarter'], periods[-1]['year'], periods[-1]['quarter']))

    everything_downloaded = False

    for period in periods:

        year = period['year']
        quarter = period['quarter']

        # Write 'data/<year>q<quarternumber>.zip'
        filename = str(year) + 'q' + str(quarter) + '.zip'
        url = 'http://www.sec.gov/data/financial-statements/' + filename
        filepath = os.path.join(target_dir, filename)

        if os.path.exists(filepath):
            print('File {} already exists at {}'.format(filename, filepath))
        else:
            print('Downloading {}  from {}  to {} ...'.format(filename, url, filepath))
            file_downloaded = False
            while file_downloaded == False:
                file_downloaded = download(url, filepath)

    # Change to more reliable : check every single file
    if period == periods[-1]:
        everything_downloaded = True
        print('Finished downloading')
    else:
        print('Something went wrong, all the files are not downloaded')

    return everything_downloaded

def download(url, filename):
    file_read = False
    file_content = ''
    online_file = None

    try:
        online_file = urllib.request.urlopen(url)

        try:
            file_content = online_file.read()
            file_read = True
        finally:
            online_file.close()

    except HTTPError as e:
        print('HTTP Error:', e.code)
    except URLError as e:
        print('URL Error:', e.code)
    except TimeoutError as e:
        print('Timeout Error:', e.code)
    except socket.timeout as e:
        print('Socket Timeout Error:', e.code)
    except http.client.IncompleteRead as e:
        print('Incomplete Read Error:', e.code)

    #write the file if completed
    if file_read:
        output_file = open(filename, 'wb')
        output_file.write(file_content)
        output_file.close()

    #try again if not completed
    else:
        print('A problem occured while downloading {}'.format(filename))
        print('Trying to download {} again'.format(filename))

    return file_read
