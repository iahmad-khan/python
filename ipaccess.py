#!/usr/local/bin/python3.3

fd = open('/var/log/httpd/access_log','r')
txt = fd.read()
print(txt)
