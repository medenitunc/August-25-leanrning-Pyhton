import pandas as pd

a = ['Apple', 'Banana', 'Orange', 'Mango ', 'Grapes']

myseries = pd.Series(a , index = ['a', 'b', 'c', 'd', 'e'])


print(myseries)
print(myseries['c'])  # Accessing element with index 'c'
print(myseries[2])    # Accessing element at position 2
