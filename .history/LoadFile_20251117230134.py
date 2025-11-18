import csv

# filedata = open('filename','mode')

'''
Operation modes:
read - r - filedata = open('filename','r')
write - w - filedata = open('filename','w')
append - a - filedata = open('filename','a')
create - x - filedata = open('filename','x')? if file not exist then create else error
'''
d = open('Sample.csv')
# print(d.read())
# print(d.readline())
# print(d.readlines())
# list1 = d.readlines()
# print(list1[4])
# dat1 = d.read()
d.close()
# print(dat1)

# f = open('Data2.csv','x') # create file
f= open('Data2.csv','w')  # write file
f.write('Name, Age, Salary\n')
f.write('John, 25, 52000\n')
f.write('Tunc, 45, 16000\n')
f.close()


# auto close
with open('Data2.csv', 'w') as f:
    f.write('Name, Age, Salary\n')
    f.write('Jenilia, 25, 52000\n')
    f.write('Raja, 45, 16000\n')

    with open('Data2.csv', 'a') as f:
       f.write('Anita, 30, 60000\n')
       f.write('Sara, 28, 48000\n') 
       f.write('Rahul, 35, 55000\n')