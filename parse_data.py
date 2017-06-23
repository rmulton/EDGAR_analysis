import os
import pandas as pd

def parse_quarter(statement_folder):
    sub_filepath = os.path.join(statement_folder, 'sub.txt')
    num_filepath = os.path.join(statement_folder, 'num.txt')
    sub = pd.read_csv(sub_filepath, delimiter='\t', lineterminator='\n', encoding='cp1252')
    num = pd.read_csv(num_filepath, delimiter='\t', lineterminator='\n', encoding='cp1252')
    # For now, let's reduce the scope
    sub = sub[sub['fp']=='FY']
    num = num[num['uom']=='USD']
    return sub, num
