#!/usr/bin/env python3
matches = 0
pre_list = []
pre_elements=0
mat_dict = {}
mat_elements=0

#opening precursor miRNA and putting base-pair sequences into a list
fhand = open("mouse_precursor_mir.fa")
for line in fhand:
    if not line.startswith(">"):
        pre_list.append(line.strip())
        pre_elements+=1

#opening mature miRNA and putting base-pair sequences into a dictionary. the KEY will be sequence, the VALUE will be # of matches in precursor mRNA
fhand = open("mouse.matureT.fa")
for line in fhand:
    if not line.startswith(">"):
        mat_dict.update({line.strip() : 0})
        mat_elements+=1

### since mature miRNA is smaller than precursor miRNA, trying to see if mature miRNA substrings are present in precursor RNA strings

for mat_seq in mat_dict:
    for pre_seq in pre_list:
        if mat_seq in pre_seq:
            matches +=1
            mat_dict[mat_seq] +=1


print matches
print mat_dict






#newdict = {"Mon":0, "Tue":0, "Wed":0, "Thu":0, "Fri": 0, "Sat":0, "Sun":0}
#for line in fhand:
#    if not line.startswith('From ') : continue 

 #   words = line.split()
    #print words[2]
  #  if words[2] in newdict:
   #     newdict[words[2]] += 1

#print newdict
