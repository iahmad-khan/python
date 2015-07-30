#!/usr/bin/python

import os, sys

path = "/root/pythoncode/fileinfo.py"

# Now get  the touple
info = os.lstat(path)

print "File Info :", info

# Now get uid of the file
print "UID of the file :%d" % info.st_uid

# Now get gid of the file
print "GID of the file :%d" % info.st_gid
