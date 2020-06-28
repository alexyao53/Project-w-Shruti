#!/usr/bin/env python3
import re #this line is necessary to use "regular functions"
fhand = open("mbox.txt")
print "Enter a regular expression: "
exp = raw_input().strip()
matches = 0

for line in fhand:
    if re.search(exp, line):
        print line
        matches += 1

print matches

