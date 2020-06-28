#!/usr/bin/env python3

print("Enter filename: ")
fhand = open(raw_input().strip()) ###have to strip last character for some reason
new_dict = {} ###make a new empty dictionary
print new_dict
for line in fhand:
    if not line.startswith('From ') : continue 

    words = line.split()
    if words[1] not in new_dict:
        new_dict[words[1]] = 1 ###makes a new key and sets the value to 1
    else:
        new_dict[words[1]] += 1 ###otherwise add 1 to the value of the existing key
print new_dict

maximum = max(new_dict, key=new_dict.get) ###max() function finds maximum value. can be used for lists too. For dictionaries, first parameter is dictionary, sceond parameter is desired key.
print maximum 
print new_dict[maximum]