import pandas as pd
# pandas - Python Data Analysis Library, dataframe manipulation and analysis


filedata = pd.read_csv('Sample.csv')
# print(filedata)
print(filedata.head())  # first 5 rows
# print(filedata.tail())  # last 5 rows
print(filedata.info())  # info about dataframe
print(filedata.describe())  # statistical summary
print(filedata['Department'].unique())  # unique values in column
# print(filedata['Department'] == 'Marketing')  # filter rows based on condition

Marketing_data = filedata[filedata['Department'] == 'Marketing']