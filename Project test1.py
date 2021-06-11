#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 20:33:36 2021

@author: kirahoriuchi
"""

import string

in_file = open("input_txt.txt", "r")
out_file = open("output_txt.txt", "w")

episode4_line = ["0", "character", "words"]
episode4_line_list = []
temp_list = []
i = 0

for line_str in in_file:
    temp_list = line_str.split(" ", 2)
    while i < 3:
        episode4_line[i] = temp_list[i].translate(str.maketrans('', '', string.punctuation))
        episode4_line[i] = episode4_line[i].strip()
        i += 1
    episode4_line_list.append(episode4_line)
    print(episode4_line, file = out_file)
    
        
#print(episode4_line)

print(episode4_line_list)
in_file.close()
out_file.close()