#!/bin/python
import re
f = open('/etc/passwd')
str = f.read()
user=raw_input('enter user: ')
pat='[\w]*'+user+'[\w]*'
match = re.findall(pat, str)
# If-statement after search() tests if it succeeded
if match:                      
      print 'found', match ## 'found word:cat'
else:
      print 'did not find'
