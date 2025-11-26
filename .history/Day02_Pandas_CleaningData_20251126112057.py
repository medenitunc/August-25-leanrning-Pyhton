import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie','Mohammed', 'Sara', None,'David', 'Nina', 'Liam'], 
    'Age': [28, 24, 22, 30, 25, 27, 23, 29,None 26, 24],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', None,'Medine', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

