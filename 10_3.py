#!/usr/bin/env python3
print("Enter filename: ")
fhand = open(raw_input().strip()) ###have to strip last character for some reason
new_dict = {"a":0, "b":0, "c":0, "d":0, "e":0} ###make a new empty dictionary
for line in fhand:
    for letter in line:
        if letter=="a" or letter=="A":
            new_dict["a"] += 1
        if letter=="b" or letter=="B":
            new_dict["b"] += 1
        if letter=="c" or letter =="C":
            new_dict["c"] += 1
        if letter=="d" or letter=="D":
            new_dict["d"] += 1
        if letter=="e" or letter=="E":
            new_dict["e"] += 1
print new_dict

t = new_dict.items() #using .items() on a dictionary turns it into a list of tuples (each pair is a tuple), and then since it's a list you can use most list functions like sort() and len()
t.sort() #sorts tuple based on value of key/value pair
print t[4] #referring to certain index of a tuple: use brackets
print t[3]
print t[2]
print t[1]
print t[0]
