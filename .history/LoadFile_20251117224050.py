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
list1 = d.readlines()
print(list1[4])



