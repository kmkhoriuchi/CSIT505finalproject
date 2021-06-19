#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:15:55 2021

@author: kirahoriuchi
"""

in_file1 = open("Episode_IV.txt", "r")
out_file1 = open("Episode_IV_out.txt", "w")
in_file2 = open("Episode_V.txt", "r")
out_file2 = open("Episode_V_out.txt", "w")
in_file3 = open("Episode_VI.txt", "r")
out_file3 = open("Episode_VI_out.txt", "w")


episode4_line_list = []
episode5_line_list = []
episode6_line_list = []
temp_list = []
quote_char = '"'

for line_str in in_file1:
    temp_list = line_str.split(" ", 2)
    episode4_line = ["0", "character", "words"]
    for elem in range(len(temp_list)):
        episode4_line[elem] = temp_list[elem].translate(str.maketrans('', '', quote_char))
        episode4_line[elem] = episode4_line[elem].strip()
        if elem == 2:
            episode4_line[elem] = episode4_line[elem].split()
            for i in range(len(episode4_line[elem])):    
                if episode4_line[elem][0].isupper() and len(episode4_line[elem][0]) > 1:
                    temp_list2 = episode4_line[elem].pop(0)
                    episode4_line[elem-1] += (' ' + temp_list2)
            episode4_line[elem] = tuple(episode4_line[elem])
            episode4_line_list.append(tuple(episode4_line))
            print(tuple(episode4_line), file = out_file1)

in_file1.close()
out_file1.close()

for line_str in in_file2:
    temp_list = line_str.split(" ", 2)
    episode5_line = ["0", "character", "words"]
    for elem in range(len(temp_list)):
        episode5_line[elem] = temp_list[elem].translate(str.maketrans('', '', quote_char))
        episode5_line[elem] = episode5_line[elem].strip()
        if elem == 2:
            episode5_line[elem] = episode5_line[elem].split()
            for i in range(len(episode5_line[elem])):    
                if episode5_line[elem][0].isupper() and len(episode5_line[elem][0]) > 1:
                    temp_list2 = episode5_line[elem].pop(0)
                    episode5_line[elem-1] += (' ' + temp_list2)
            episode5_line[elem] = tuple(episode5_line[elem])
            episode5_line_list.append(tuple(episode5_line))
            print(tuple(episode5_line), file = out_file2)

in_file2.close()
out_file2.close()

for line_str in in_file3:
    temp_list = line_str.split(" ", 2)
    episode6_line = ["0", "character", "words"]
    for elem in range(len(temp_list)):
        episode6_line[elem] = temp_list[elem].translate(str.maketrans('', '', quote_char))
        episode6_line[elem] = episode6_line[elem].strip()
        if elem == 2:
            episode6_line[elem] = episode6_line[elem].split()
            for i in range(len(episode6_line[elem])):    
                if episode6_line[elem][0].isupper() and len(episode6_line[elem][0]) > 1:
                    temp_list2 = episode6_line[elem].pop(0)
                    episode6_line[elem-1] += (' ' + temp_list2)
            episode6_line[elem] = tuple(episode6_line[elem])
            episode6_line_list.append(tuple(episode6_line))
            print(tuple(episode6_line), file = out_file3)

in_file3.close()
out_file3.close()
