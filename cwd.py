#!/bin/python
# Using os module to change and display directries

import os
print os.getcwd() #cwd=current working directory
os.chdir("/root")
print os.getcwd()
dirlist = os.listdir('.')  # finally get listing of cwd
for file in dirlist:
    print file

