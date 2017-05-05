import os
import urllib.request
from urllib.error import *
import Tools
from socket import timeout
from http.client import IncompleteRead

def edgar_download(periods_to_download):

    print("Start downloading from year {} quarter {} to year {} to quarter {}".format(periods_to_download[0]['year'], periods_to_download[0]['quarter'], periods_to_download[-1]['year'], periods_to_download[-1]['quarter']))

    everything_downloaded = False

    for period in periods_to_download:

        year = period['year']
        quarter = period['quarter']
        # Create year directory if not existing
        target_dir = 'EDGAR_data/'+str(year)+'/'
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Write 'EDGAR_data/<year>/inancial_statements_year_q<quarternumber>.zip'
        url = 'http://www.sec.gov/data/financial-statements/' + str(year) + 'q' + str(quarter) + '.zip'
        filepath = target_dir+'financial_statements_' + str(year) + '_q' + str(quarter) + '.zip'
        file_downloaded = False
        while file_downloaded == False:
            file_downloaded = download(url, filepath)

        if period == periods_to_download[-1]:
            everything_downloaded = True
            print('Downloaded !')
    
    return(everything_downloaded)

def download(url, filename):
    file_read = False
    file_content = ''
    online_file = None

    if os.path.isfile(filename):
        print(filename + ' already exists')

    else:
        print('Downloading :', url)

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
            print('A problem occured while downloading the file : ' + filename)
            print('Retrying to download the file')

        return(file_read)
