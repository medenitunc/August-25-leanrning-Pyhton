import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie','Mohammed', 'Sara', None,'David', 'Nina', 'Liam'], 
    'Age': [28, 24, 22, 30, 25, 27, 23, 29,None, 26, 24],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix','Medine',None, 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)


# to detect null values , isnull() or notnull()
print("\n Detecting null values:\n", df.isnull())

print("\n We are having null values in 'Name' column:\n", df['Name'].isnull())

print("\nNo of null values in data:\n", df.isnull().sum().sum())
