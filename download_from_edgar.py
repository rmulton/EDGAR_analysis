# -*-coding:Latin-1 -*

'''
Module:     'download_from_edgar'
Aim:        Downloads the required data from SEC's EDGAR database (.zip file)
Functions:  - dowload_edgar_period
            - download_and_save
'''

################################################################################

## import the required modules and errors
import os
import urllib.request
from urllib.error import *
import socket
from socket import timeout
from socket import gaierror
import http

################################################################################

def download_edgar_period(quarters_list):

    '''
    Downloads data from EDGAR database for the period input.
    quarters_list must be a list of tuples as in this example:[ (2014,1), (2014,2) ]
    '''

    # downloads the files for every period required
    for year_quarter in quarters_list:

        # creates year's directory if not existing
        year = year_quarter[0]
        quarter = year_quarter[1]
        target_dir = 'edgar_data/'+str(year)+'/'
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # the accurate url to download the file
        url = 'https://www.sec.gov/data/financial-statements/' + str(year)    \
               + 'q' + str(quarter) + '.zip'

        # if the file doesn't exist yet download and save it
        file_name = target_dir + str(year) + '_q' + str(quarter) + '.zip'
        download_and_save(url, file_name) # this function ensures download is complete

################################################################################

def download_and_save(url, file_name):

    '''
    Downloads the file from the url and save it in file_name path if not existing.
    Repeats until the job is done
    '''

    # variable to check that the job is done
    file_saved = False

    # no download if the file doesn't exist
    if os.path.isfile(file_name):
        print(file_name + ' already downloaded')

    else:
        print('Downloading ', url)

        # repeats until the job is done
        while file_saved == False:

            try:
                # loads the file
                online_file = urllib.request.urlopen(url)
                file_content = online_file.read()
                online_file.close()

                # saves the file
                output_file = open(file_name, 'wb')
                output_file.write(file_content)
                output_file.close()

                # indicates that the job is done
                file_saved = True

            except HTTPError as e:
                print('HTTP Error', e.code)

            except URLError as e:
                print('URL Error', e.code)

            except TimeoutError as e:
                print('Timeout Error', e.code)

            except socket.timeout as e:
                print('Socket Timeout Error', e.code)

            except http.client.IncompleteRead as e:
                print('Incomplete Read Error', e.code)

            except socket.gaierror as e:
                print('Gai error', e.code)

################################################################################
