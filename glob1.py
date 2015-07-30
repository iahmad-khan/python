#!/bin/python
# Using glob to list files

import glob
files = glob.glob("*.py")
#print files 
for f in files:
    print f
