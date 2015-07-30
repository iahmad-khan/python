#!/bin/python
import socket
host = raw_input("Enter a host to resolve\n")
result = socket.gethostbyname(host)
print "The ip address of host is: ", result
