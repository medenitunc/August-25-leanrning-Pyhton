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
print("\n Testing Empl \n",testingemp)    # Accessing elements with specified indices, including a missing index

#onedimensional series
#multidimensional dataframe

data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
    'Age': [28, 24, 22, 30, 25], 
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)
print("\n Dataframe \n",df) 
