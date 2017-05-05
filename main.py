import download_data
import period
import unzip
import parse_data
from DataFolder import DataFolder
import os
STARTING_YEAR = 2015
STARTING_QUARTER = 1
ENDING_YEAR = 2016
ENDING_QUARTER = 1

# Weird MSoft stuff
os.chdir('C:\\Users\\robin\\Desktop\\edgar_analysis')
directory = 'C:\\Users\\robin\\Desktop\\edgar_analysis\\edgar_data'

DataFolder = DataFolder(directory)
period = period.period(STARTING_YEAR, STARTING_QUARTER, ENDING_YEAR, ENDING_QUARTER)

download_data.edgar_download(period)
unzip.unzip_everything(DataFolder.get_data_folder_path())
parse_data.parse_all(DataFolder, period)
