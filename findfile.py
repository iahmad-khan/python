#!/bin/python
# Finding files using os.walk and regex

import os,re,sys
patt = sys.argv[1]

def findfile(filepattern, base = '/root'):
    regex = re.compile(filepattern)
    matches = []
    for root,dirs,files in os.walk(base):
        for f in files:
          if regex.match(f):
             matches.append(root + '/' + f)
    return matches 

m = findfile(patt,'/root')
for f in m:
    print f
