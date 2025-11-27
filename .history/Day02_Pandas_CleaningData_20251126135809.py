import pandas as pd

data = {
    'DasId': ['A348756', 'A348757', 'A348758', 'A348759', 'A348760','A348761', 'A348762', 'A348763', 'A348764', 'A348756', 'A348765'],
    'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie','Mohammed', 'Sara', None,'David', 'John', 'Liam'], 
    'Age': [28, 24, 22, 30, 25, 27, 23, 29,None, 28, 24],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix','Medine',None, 'San Antonio', 'San Diego', 'New York', 'San Jose']
}

df = pd.DataFrame(data)
# print("Original DataFrame:\n", df)


# to detect null values , isnull() or notnull()
# print("\n Detecting null values:\n", df.isnull())

# print("\n We are having null values in 'Name' column:\n", df['Name'].isnull())

# print("\nNo of null values in data:\n", df.isnull().sum().sum())

df1 = df.dropna()  # Drop rows with any null values

# print("\n DataFrame after dropping rows with null values:\n", df1)

df2 = df.fillna(0)  # Fill null values with 0

# print("\n DataFrame after filling null values with 0:\n", df2)

df3 = df[['DasId','Name', 'Age','City']].fillna({'Name': 'No name', 'Age': df['Age'].mean(), 'City': 'No city'})  # Fill null values in 'Name' and 'Age' columns with 0]'Age'].fillna(df['Age'].mean())  # Fill null values in 'Age' column with the mean age

# print("\n DataFrame after filling null values with specific values:\n", df3)


# To check for duplicate rows
print("\n Checking for duplicate rows:\n", df3.duplicated())

df3 = df3.drop_duplicates()  # Remove duplicate rows
print("\n DataFrame after removing duplicate rows:\n", df3)

# print(df3['DasId'].duplicated())  # Check for duplicate DasId values
# print(df3[df3['DasId'].duplicates(keep='first')])  # Remove duplicate rows based on 'DasId' column

df3 = df3.drop_duplicates(subset=['DasId'], keep='first')  # Remove duplicate rows based on 'DasId' column
print("\n DataFrame after removing duplicate DasId rows:\n", df3)

df3['Age'] = df3['Age'].astype(int)  # Convert 'Age' column to integer type
print("\n DataFrame after converting 'Age' to integer type:\n", df3)

df3['City'] = df3['City'].str.upper()  # Convert 'City' column to uppercase
print("\n DataFrame after converting 'City' to uppercase:\n", df3)

df3[['Name', 'City']] = df3[['Name', 'City']].apply(lambda x: x.str.upper())  # Remove leading/trailing whitespace from 'Name' and 'City' columns
print("\n DataFrame after stripping whitespace from 'Name' and 'City':\n", df3)
