import download_data
import period
import unzip
import parse_data
from DataFolder import DataFolder
import os
import compute_ratios

STARTING_YEAR = 2015
STARTING_QUARTER = 1
ENDING_YEAR = 2015
ENDING_QUARTER = 2

def main(STARTING_YEAR, STARTING_QUARTER, ENDING_YEAR, ENDING_QUARTER, directory):
    os.chdir('C:\\Users\\robin\\Desktop\\edgar_analysis')
    directory = 'C:\\Users\\robin\\Desktop\\edgar_analysis\\edgar_data'

    data_folder = DataFolder(directory)
    required_period = period.period(STARTING_YEAR, STARTING_QUARTER, ENDING_YEAR, ENDING_QUARTER)

    download_data.edgar_download(required_period)
    unzip.unzip_everything(data_folder.get_data_folder_path())
    sub, num = parse_data.parse_all(data_folder, required_period)
    assets, liabilities, liquidity = compute_ratios.compute_ratios(sub, num)
    return assets, liabilities, liquidity