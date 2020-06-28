#!/usr/bin/env python3
import re #this line is necessary to use "regular functions"
print "Enter filename: "
fhand = open(raw_input().strip())
print "Enter a regular expression: " #enter "New Revision:" without the quotes
exp = raw_input().strip()
matches = 0
total = 0

#for line in fhand:
    #if re.search(exp, line):
        #print line
        #matches += 1
        
for line in fhand: 
    line = line.rstrip() 
    x = re.findall('ˆNew Revision:.*rev=([0-9]+)', line) 
    if len(x) > 0: 
        print x


print matches
