
import os
import pandas as pd

path = 'C:\\Users\\TueHellstern\\Dropbox\\KEA\\BE_IT\\4_2\\Curvex\\KEA\\Curvex_data\\data\\frequencies_and_metrics\\1'
file_extension = '.csv'

csv_file_list = []

for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith(file_extension):
            file_path = os.path.join(root, name)
            csv_file_list.append(file_path)

dfs = [pd.read_csv(f) for f in csv_file_list]

print(dfs)


