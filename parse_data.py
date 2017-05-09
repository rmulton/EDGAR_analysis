import pandas as pd

def parse_all(data_folder, period):
	for el in period:
		statement_folder_path = data_folder.get_statement_path(el['year'], el['quarter'])
		return parse_quarter(statement_folder_path)

def parse_quarter(statement_folder_path):
	sub_filepath = statement_folder_path + 'sub.txt'
	num_filepath = statement_folder_path + 'num.txt'
	sub = pd.read_csv(sub_filepath, delimiter='\t', lineterminator='\n', encoding='cp1252')
	num = pd.read_csv(num_filepath, delimiter='\t', lineterminator='\n', encoding='cp1252')
	# For now, let's reduce the scope
	sub = sub[sub['fp']=='FY']
	num = num[num['uom']=='USD']
	return sub, num