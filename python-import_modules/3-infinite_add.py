#!/usr/bin/python3
import sys
res = 0
for i in range(1, len(sys.argv)):
    res = res + int(sys.argv[i])
print(res)
