#!/bin/python

import os

cmd = "grep '^ijaz' /etc/group | awk -F: '{print $4}'"

os.system(cmd)
