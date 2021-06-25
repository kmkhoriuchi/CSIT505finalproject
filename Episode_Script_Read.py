#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:15:55 2021

@author: kirahoriuchi
"""
from Sentiment_Import import positive_word_bank
from Sentiment_Import import negative_word_bank
import string

positive_sent = positive_word_bank
negative_sent = negative_word_bank


in_file1 = open("Episode_IV.txt", "r")
out_file1 = open("Episode_IV_out.txt", "w")
in_file2 = open("Episode_V.txt", "r")
out_file2 = open("Episode_V_out.txt", "w")
in_file3 = open("Episode_VI.txt", "r")
out_file3 = open("Episode_VI_out.txt", "w")

epi4_line_list = []
epi4_script = []
epi4_char_key = []
epi4_script_bank = []

temp_list = []
quote_char = '"'

# Episode 4
# Importing Episode 4 script from file.
for line_str in in_file1:
    temp_list = line_str.split(" ", 2)
    epi4_line = ["0", "character", "words"]
    for elem in range(len(temp_list)):
        epi4_line[elem] = temp_list[elem].translate(str.maketrans('', '', quote_char))
        epi4_line[elem] = epi4_line[elem].strip()
        if elem == 2:
            epi4_line[elem] = epi4_line[elem].split()
            for i in range(len(epi4_line[elem])):
                if epi4_line[elem][0].isupper() and len(epi4_line[elem][0]) > 1:
                    temp_list2 = epi4_line[elem].pop(0)
                    epi4_line[elem-1] += (' ' + temp_list2)
            epi4_line[elem] = tuple(epi4_line[elem])
            epi4_line_list.append(tuple(epi4_line))
            print(tuple(epi4_line), file = out_file1)

#Sorting Episode 4 lines by character
for item in range(len(epi4_line_list)):
    temp_lines = [' ', []]
    if epi4_line_list[item][1] not in epi4_char_key:
        epi4_char_key.append(epi4_line_list[item][1])
        temp_lines[0] = epi4_line_list[item][1]
        temp_lines[1].append(epi4_line_list[item][2])
        epi4_script.append(temp_lines)
    else:
        for i in range(0, len(epi4_script)):
            if epi4_script[i][0] == epi4_line_list[item][1]:
                epi4_script[i][1].append(epi4_line_list[item][2])
            
for item in range(len(epi4_script)):
    epi4_script_bank.append(epi4_script[item][1])

#Creating Episode 4 dictionary: keys are characters, values are a list of character lines in tuples.                
episode4_dict = dict(zip(epi4_char_key, epi4_script_bank))
#print(key , ':', len(episode4_dict[key]), "Lines")

positive_count_list = []
negative_count_list = []
epi4_dict_copy = episode4_dict.copy()

#Create a copy of Episode 4 dictionary
for key in epi4_dict_copy:
    for i in range(len(epi4_dict_copy[key])):
        epi4_dict_copy[key][i] = list(epi4_dict_copy[key][i])

#Attempt to analyze if words in character lines are positive or negative.
for char in range(len(episode4_dict)):
    positive_count_list_item = [' ', 0]
    negative_count_list_item = [' ', 0]
    positive_count_list_item[0] = epi4_char_key[char]
    negative_count_list_item[0] = epi4_char_key[char]
    for key in epi4_dict_copy:
        for i in range(len(epi4_dict_copy[key])):
            positive_count = 0
            negative_count = 0
            for j in range(len(epi4_dict_copy[key][i])):
                temp_word = epi4_dict_copy[key][i][j].translate(str.maketrans('', '', string.punctuation))
                temp_word = temp_word.lower()
                if temp_word in positive_sent:
                    positive_count += 1
                elif temp_word in negative_sent:
                    negative_count += 1
            positive_count_list_item[1] = positive_count
            negative_count_list_item[1] = negative_count
    positive_count_list.append(positive_count_list_item)
    negative_count_list.append(negative_count_list_item)


in_file1.close()
out_file1.close()

#Episode 5
epi5_line_list = []
epi5_char_key = []
epi5_script = []
epi5_script_bank = []

#Importing Episode 5 script from file.
for line_str in in_file2:
    temp_list = line_str.split(" ", 2)
    epi5_line = ["0", "character", "words"]
    for elem in range(len(temp_list)):
        epi5_line[elem] = temp_list[elem].translate(str.maketrans('', '', quote_char))
        epi5_line[elem] = epi5_line[elem].strip()
        if elem == 2:
            epi5_line[elem] = epi5_line[elem].split()
            for i in range(len(epi5_line[elem])):    
                if epi5_line[elem][0].isupper() and len(epi5_line[elem][0]) > 1:
                    temp_list2 = epi5_line[elem].pop(0)
                    epi5_line[elem-1] += (' ' + temp_list2)
            epi5_line[elem] = tuple(epi5_line[elem])
            epi5_line_list.append(tuple(epi5_line))
            print(tuple(epi5_line), file = out_file2)
            
# Sorting Episode 5 script line by character.            
for item in range(len(epi5_line_list)):
    temp_lines = [' ', []]
    if epi5_line_list[item][1] not in epi5_char_key:
        epi5_char_key.append(epi5_line_list[item][1])
        temp_lines[0] = epi5_line_list[item][1]
        temp_lines[1].append(epi5_line_list[item][2])
        epi5_script.append(temp_lines)
    else:
        for i in range(0, len(epi5_script)):
            if epi5_script[i][0] == epi5_line_list[item][1]:
                epi5_script[i][1].append(epi5_line_list[item][2])
            
for item in range(len(epi5_script)):
    epi5_script_bank.append(epi5_script[item][1])

#Create Episode 5 dictionary where keys are characters and values are a list of character lines in tuples.                 
episode5_dict = dict(zip(epi5_char_key, epi5_script_bank))

positive_count_list = []
negative_count_list = []
epi5_dict_copy = episode5_dict.copy()

#Create a copy of Episode 5 dictionary
for key in epi5_dict_copy:
    for i in range(len(epi5_dict_copy[key])):
        epi5_dict_copy[key][i] = list(epi5_dict_copy[key][i])

#Attempt to analyze character lines by positive or negative sentiment.
for char in range(len(episode5_dict)):
    positive_count_list_item = [' ', 0]
    negative_count_list_item = [' ', 0]
    positive_count_list_item[0] = epi5_char_key[char]
    negative_count_list_item[0] = epi5_char_key[char]
    for key in epi5_dict_copy:
        for i in range(len(epi5_dict_copy[key])):
            positive_count = 0
            negative_count = 0
            for j in range(len(epi5_dict_copy[key][i])):
                temp_word = epi5_dict_copy[key][i][j].translate(str.maketrans('', '', string.punctuation))
                temp_word = temp_word.lower()
                if temp_word in positive_sent:
                    positive_count += 1
                elif temp_word in negative_sent:
                    negative_count += 1
            positive_count_list_item[1] = positive_count
            negative_count_list_item[1] = negative_count
    positive_count_list.append(positive_count_list_item)
    negative_count_list.append(negative_count_list_item)
       

in_file2.close()
out_file2.close()

#Episode 6

epi6_line_list = []
epi6_char_key = []
epi6_script = []
epi6_script_bank = []

# Import Episode 6 script from file.
for line_str in in_file3:
    temp_list = line_str.split(" ", 2)
    epi6_line = ["0", "character", "words"]
    for elem in range(len(temp_list)):
        epi6_line[elem] = temp_list[elem].translate(str.maketrans('', '', quote_char))
        epi6_line[elem] = epi6_line[elem].strip()
        if elem == 2:
            epi6_line[elem] = epi6_line[elem].split()
            for i in range(len(epi6_line[elem])):    
                if epi6_line[elem][0].isupper() and len(epi6_line[elem][0]) > 1:
                    temp_list2 = epi6_line[elem].pop(0)
                    epi6_line[elem-1] += (' ' + temp_list2)
            epi6_line[elem] = tuple(epi6_line[elem])
            epi6_line_list.append(tuple(epi6_line))
            print(tuple(epi6_line), file = out_file3)
            
#Sort script lines by character.           
for item in range(len(epi6_line_list)):
    temp_lines = [' ', []]
    if epi6_line_list[item][1] not in epi6_char_key:
        epi6_char_key.append(epi6_line_list[item][1])
        temp_lines[0] = epi6_line_list[item][1]
        temp_lines[1].append(epi6_line_list[item][2])
        epi6_script.append(temp_lines)
    else:
        for i in range(0, len(epi6_script)):
            if epi6_script[i][0] == epi6_line_list[item][1]:
                epi6_script[i][1].append(epi6_line_list[item][2])
            
for item in range(len(epi6_script)):
    epi6_script_bank.append(epi6_script[item][1])
                
#Create Episode 6 dictionary where keys are characters values are a list of character lines in tuples.      
episode6_dict = dict(zip(epi6_char_key, epi6_script_bank))

positive_count_list = []
negative_count_list = []
epi6_dict_copy = episode6_dict.copy()

#Copy Episode 6 dictionary
for key in epi6_dict_copy:
    for i in range(len(epi6_dict_copy[key])):
        epi6_dict_copy[key][i] = list(epi6_dict_copy[key][i])

#Attempt to analyze Episode 6 dictionary by positive and negative sentiment.
for char in range(len(episode6_dict)):
    positive_count_list_item = [' ', 0]
    negative_count_list_item = [' ', 0]
    positive_count_list_item[0] = epi6_char_key[char]
    negative_count_list_item[0] = epi6_char_key[char]
    for key in epi6_dict_copy:
        for i in range(len(epi6_dict_copy[key])):
            positive_count = 0
            negative_count = 0
            for j in range(len(epi6_dict_copy[key][i])):
                temp_word = epi6_dict_copy[key][i][j].translate(str.maketrans('', '', string.punctuation))
                temp_word = temp_word.lower()
                if temp_word in positive_sent:
                    positive_count += 1
                elif temp_word in negative_sent:
                    negative_count += 1
            positive_count_list_item[1] = positive_count
            negative_count_list_item[1] = negative_count
    positive_count_list.append(positive_count_list_item)
    negative_count_list.append(negative_count_list_item)

in_file3.close()
out_file3.close()
