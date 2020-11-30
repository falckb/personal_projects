import pandas as pd
import urllib.request
import glob


def grab_files_from_yearly_urls(base_url, start_year, end_year):
    """
    Take a list of years, for each of those years, append year to end of url link, download each of those files into a csv
    """
    print('Downloading files from ' + base_url + '...')
    for year in range(start_year, end_year):
        urllib.request.urlretrieve(base_url+str(year), f'/Users/User/Documents/Work/Interviews/Velocity/ahr{year}.csv')
    print('Files downloaded.')


def grab_files_from_disk(path):
    """
    For each file in a certain a specified path, read the csv and append it to the dataframe, then add that to empty list of files
    """
    files = []
    for file in glob.glob(path):
        data = pd.read_csv(file, index_col=None)
        files.append(data)
    return files
