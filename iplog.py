#!/bin/python

with open('/var/log/httpd/access_log' ,'r') as f:
    result = dict()
    for line in f:
        #print line
        line = line.split()
        ip = line[0]
        print ip
       # if '200' in line:
        result[ip]=result.setdefault(ip,0)+1
    for ip , count in sorted(result.items(), key = lambda x: x[1], reverse=True)[1:10]:
       print ip , count        
