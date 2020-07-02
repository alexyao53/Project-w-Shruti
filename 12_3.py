#!/usr/bin/env python3
import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt') 
char = 0
for line in fhand: 
    print line.strip()
    for character in line:
        char += 1
    if char > 3000:
        break

print char