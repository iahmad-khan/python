#!/bin/python

from sys import argv

import grp

group = grp.getgrnam(in_group)

members=group.gr_mem

for mem in members:
	print mem 
