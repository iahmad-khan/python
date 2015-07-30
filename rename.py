#!/bin/python
""" This code renames all the files given a pattren and path"""

import os
import glob as g

for f in g.glob('/root/pythoncode/test/*.txt'):
    newname = f.replace('.txt','.py')
    os.rename(f,newname)

print 'done'

