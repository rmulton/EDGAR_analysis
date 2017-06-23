import pickle
import argparse
import download_data
import period
import unzip
import parse_data
import os
import compute_ratios

def main(periods, data_folder):

    download_data.download_edgar(periods, data_folder)
    unzip.unzip_everything(data_folder)

    for el in os.listdir(data_folder):
        if el[-4:]!='.zip':
            quarter = os.path.join(data_folder, el)
            print('Computing ratios for {}'.format(quarter))
            quarter_folder = os.path.join(data_folder, quarter)
            sub, num = parse_data.parse_quarter(quarter)
            ratios = compute_ratios.compute_quarter(sub, num)
            result_path = os.path.join(quarter, 'ratios.pickle')
            pickle.dump(ratios, open(result_path, 'wb'))
            print('Results saved in {}'.format(result_path))

if __name__=='__main__':
    
    parser = argparse.ArgumentParser()

    parser.add_argument('--starting', type=tuple, default=(2015, 1), help='(year, quarter) tuple from wich you want to download data')
    parser.add_argument('--to', type=tuple, default=(2015, 4), help='(year, quarter) tuple until wich you want to download data')
    parser.add_argument('--data_folder', type=str, default='data', help='Folder that is going to contain the data')

    args = parser.parse_args()

    periods = period.period(args.starting, args.to)

    main(periods, args.data_folder)
