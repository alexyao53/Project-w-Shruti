#!/usr/bin/env python3
import os 
from os.path import join 
mp3_dict = {}
for (dirname, dirs, files) in os.walk('.'): 
    for filename in files: 
        if filename.endswith('.mp3') : 
            thefile = os.path.join(dirname,filename) 
            print os.path.getsize(thefile), thefile
            for value in mp3_dict:
                if os.path.getsize(thefile) in mp3_dict:
                    print thefile
            mp3_dict[thefile] = os.path.getsize(thefile)

print mp3_dict
