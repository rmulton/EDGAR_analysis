import os

class DataFolder:
    def __init__(self, data_folder_path):
        self.data_folder_path = data_folder_path
        if not os.path.exists(self.data_folder_path):
            os.makedirs(self.data_folder_path)
    
    def get_data_folder_path(self):
        return self.data_folder_path
    
    def get_statement_path(self, year, quarter):
        output = self.data_folder_path
        output += '\\' + str(year)
        output += '\\financial_statements_' + str(year)
        output += '_q' + str(quarter) + '\\'
        return output