#!/usr/bin/env python3
fhand = open("mbox.txt")
newdict = {"Mon":0, "Tue":0, "Wed":0, "Thu":0, "Fri": 0, "Sat":0, "Sun":0}
for line in fhand:
    if not line.startswith('From ') : continue 

    words = line.split()
    #print words[2]
    if words[2] in newdict:
        newdict[words[2]] += 1

print newdict
