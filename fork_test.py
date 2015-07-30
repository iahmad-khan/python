#!/usr/bin/python

import os
pid = os.fork()
if pid == 0: # the child
     print "this is the child"
elif pid > 0:
     print "the child is pid %d" % pid
else:
    print("An error occured")
