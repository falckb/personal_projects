import pandas as pd
from ahr_file_retrieve import grab_files_from_yearly_urls
from ahr_file_retrieve import grab_files_from_disk


baseurl = 'https://www.americashealthrankings.org/api/v1/downloads/report/1/'


# Export to csv for use in Power BI
if __name__ == "__main__":
    
    # Download all relevant files from baseurl
    grab_files_from_yearly_urls(baseurl, 1991, 2015)

    # Gather all files to concatenate
    files = grab_files_from_disk('/Users/User/Documents/Work/Interviews/Velocity/ahr*')
    df = pd.concat(files, axis=0, ignore_index=True)
    
    # Make necessary filtering adjustments to gather only annual obesity stats
    df = df.loc[df['Measure Name'] == 'Obesity']
    df = df.filter(['Edition', 'Measure Name', 'State Name', 'Value'])
    df['Edition'] = '12/31/' + df['Edition'].astype(str)
    df['Value'] = df['Value'].astype(float) / 100    
    
    # To CSV
    df.to_csv('/Users/User/Documents/Work/Interviews/Velocity/ahr_concat1.csv', index=False)
    print('Done.')