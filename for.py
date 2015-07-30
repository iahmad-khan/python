#!/bin/python

inf = file('csv','r')

for f in inf.readlines():
    print f.rstrip()

inf.close
