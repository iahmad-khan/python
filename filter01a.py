#!/bin/python3

import sys
import re

pattern = 'ijaz'
regexp = re.compile(pattern)

for line in sys.stdin:
    result = regexp.search(line)
    if result :
        sys.stdout.write(line)
        break
