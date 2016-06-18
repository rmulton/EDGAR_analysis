import download_from_edgar
import unzip_files
import user_interface
import tools

##############################################################################################

# Step 0 : Ask the inputs
from_year,from_quarter, to_year, to_quarter = user_interface.ask_inputs()
list_of_quarter = tools.year_quarter_list(from_year,from_quarter, to_year, to_quarter)

##############################################################################################

# Step 1: download the files, save it and unzip it
download_from_edgar.download_edgar_period(list_of_quarter)
unzip_files.unzip_everything()

##############################################################################################
