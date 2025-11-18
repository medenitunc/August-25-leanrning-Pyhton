import pandas as pd
# pandas - Python Data Analysis Library, dataframe manipulation and analysis


filedata = pd.read_csv('Sample.csv')
# print(filedata)
print(filedata.head())  # first 5 rows
# print(filedata.tail())  # last 5 rows
print(filedata.info())  # info about dataframe
print(filedata.describe())  # statistical summary


