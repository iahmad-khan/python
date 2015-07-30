#!/bin/python

import csv
sum=0
count=0
with open('csv', 'rb') as f:
    mycsv = csv.reader(f)
    for row in mycsv:
        sum += int(row[2])
        count +=1

if count !=0:
   print 'The avg is : ', sum/count
else:
   print 'The avg doesnt exist'
