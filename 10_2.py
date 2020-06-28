#!/usr/bin/env python3

print("Enter filename: ")
fhand = open(raw_input().strip()) ###have to strip last character for some reason
new_dict = {} ###make a new empty dictionary
print new_dict
for line in fhand:
    if not line.startswith('From ') : continue 

    words = line.split()
    atpos = words[5].find(':') - 2
    sppos = words[5].find(" ", atpos)
    time = words[5][atpos:atpos + 2]
    if time not in new_dict:
        print time
        new_dict[time] = 1 ###makes a new key and sets the value to 1
    else:
        new_dict[time] += 1 ###otherwise add 1 to the value of the existing key
print new_dict

t = new_dict.items() #using .items() on a dictionary turns it into a list of tuples (each pair is a tuple), and then since it's a list you can use most list functions like sort() and len()
t.sort()
print t