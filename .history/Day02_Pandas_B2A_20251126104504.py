import pandas as pd

a = ['Apple', 'Banana', 'Orange', 'Mango ', 'Grapes']

myseries = pd.Series(a , index = ['a', 'b', 'c', 'd', 'e'])


# print(myseries)
# print(myseries['c'])  # Accessing element with index 'c'

emp = {'A109838': 'John', 'A109839': 'Alice', 'A109840': 'Bob' , 'A109841': 'Eve', 'A109842': 'Charlie'}

empseries = pd.Series(emp)
print(empseries)    
print(empseries['A109840'])  # Accessing element with index 'A109840'

testingemp = pd.Series(emp, index = ['A109838', 'A109842'])
print(testingemp)    # Accessing elements with specified indices, including a missing index