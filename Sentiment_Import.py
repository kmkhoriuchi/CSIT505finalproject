#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 14:40:03 2021

@author: kirahoriuchi
"""

in_file1 = open("positive_words_en.txt", "r")
out_file1 = open("positive_words_bank.txt", "w")
in_file2 = open("negative_words_en.txt", "r")
out_file2 = open("negative_words_bank.txt", "w")

positive_list = []
negative_list = []


for line_str in in_file1:
    temp_str = line_str
    temp_str = temp_str.strip()
    positive_list.append(temp_str)
    print(temp_str, file = out_file1)
    
positive_word_bank = tuple(positive_list)
print(len(positive_word_bank), "positive words")

in_file1.close()
out_file1.close()

for line_str in in_file2:
    temp_str = line_str
    temp_str = temp_str.strip()
    negative_list.append(temp_str)
    print(temp_str, file = out_file2)
    
negative_word_bank = tuple(negative_list)
print(len(negative_word_bank), "negative words")

in_file2.close()
out_file2.close()


    