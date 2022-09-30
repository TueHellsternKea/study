# Import
import os
import glob
import pandas as pd

# Part setup
#path = r'C:\\Users\\TueHellstern\\Dropbox\\KEA\\BE_IT\\4_2\\Curvex\\KEA\\Curvex_data\\data\\frequencies_and_metrics\\1\\'
path = r'C:\\Users\\tuehe\\Dropbox\\KEA\\BE_IT\\4_2\\Curvex\\KEA\\Curvex_data\\data\\raw_EEG_data\\'

# Get all csv files including path
all_csv = glob.glob(path + '/**/*.csv', recursive=True)

# Combine all csv files in one dataframe
dataframe = pd.concat(map(pd.read_csv, all_csv), ignore_index=True)

# Export dataframe
dataframe.to_csv(path + 'all_csv_files.csv', sep=';', index=False)