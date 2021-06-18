#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:57:33 2021

@author: kirahoriuchi
"""

in_file1 = open("Episode_IV_out.txt", "r")
char_set = {''}


for in_tuple in in_file1:
    temp_tuple = in_tuple
    print(temp_tuple)
    char_list = ['char', 'line']
    char_list[0] = temp_tuple[1]
    char_list[1] = temp_tuple[2]
    
    char_line_list = [char_list[0], []]
    
    if char_list[0] in char_set:
        char_line_list[1].append(char_list[1])
    else:
        char_set.add(char_list[0])
        char_line_list.append(char_list)

episode4_char_dict = dict(zip(char_set, char_line_list[1]))
print(episode4_char_dict)
        
in_file1.close()