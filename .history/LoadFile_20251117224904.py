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

f = open('Data1.csv','x') # create file
f= open('Data1.csv','w')  # write file
f.write('Name, Age, Salary\n')
f.write('Giri, 25, 52000\n')
f.write('Medeni, 45, 16000\n')
f.close()


