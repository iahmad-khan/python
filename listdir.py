#!/usr/bin/python

import os, sys

# Open a file
path = "/root/pythoncode"
dirs = os.listdir( path )
#print dirs
# This would print all the files and directories
for file in dirs:
    print file
