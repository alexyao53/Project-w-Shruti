#!/usr/bin/env python3

######how to find a certain character in a string:
#data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#atpos = data.find('@') ###.find(" ") returns index of desired character
#print atpos

#sppos = data.find(' ', atpos)
#print sppos

#host = data[atpos+1:sppos]
#print host

print("Enter filename: ")
fhand = open(raw_input().strip()) ###have to strip last character for some reason
new_dict = {} ###make a new empty dictionary
print new_dict
for line in fhand:
    if not line.startswith('From ') : continue 

    words = line.split()
    if words[1] not in new_dict:
        atpos = words[1].find('@')
        sppos = words[1].find(" ", atpos)
        domain = words[1][atpos+1:sppos]
        print domain
        new_dict[domain] = 1 ###makes a new key and sets the value to 1
    else:
        new_dict[domain] += 1 ###otherwise add 1 to the value of the existing key
print new_dict


