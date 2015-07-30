#!/bin/python
import os
pattren = raw_input("Enter a letter or pattern: ")
cmd = 'grep ' + pattren + ' /etc/passwd | awk -F: \'{print $1}\''
os.system(cmd)
