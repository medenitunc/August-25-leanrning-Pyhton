# read
# import pandas as pd


import pandas as pd

df = pd.read_csv('SalesData.csv')
# print(df)
# print(df.head())  # first 5 rows
# print(df.tail())  # last 5 rows
# print(df.tail(3))  # last 3 rows
# print(df.head(2))  # first 2 rows

# print(df.shape)  # Number of rows and columns
# print(df.info())  # info about dataframe

# print(df.columns)  # column names   

# print(df.dtypes)  # data types of each column

print(df['Sales'])  # specific column data



