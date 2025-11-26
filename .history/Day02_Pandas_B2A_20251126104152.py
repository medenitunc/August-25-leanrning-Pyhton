import pandas as pd

a = ['Apple', 'Banana', 'Orange', 'Mango ', 'Grapes']

myseries = pd.Series(a , index = ['a', 'b', 'c', 'd', 'e'])


# print(myseries)
# print(myseries['c'])  # Accessing element with index 'c'

emp = {'A109838': 'John', 'A109839': 'Alice', 'A109840': 'Bob' , 'A109841': 'Eve', 'A109842': 'Charlie'}

empseries = pd.Series(emp)
print(empseries)    
print(empseries['A109840'])  # Accessing element with index 'A109840'
print(empseries['A109838':'A109841'])  # Slicing from index 'A109838' to 'A109841'