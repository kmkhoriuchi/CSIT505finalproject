#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:06:45 2021

@author: kirahoriuchi
"""
from matplotlib import pyplot as plt_ep4
from matplotlib import pyplot as plt_ep5
from matplotlib import pyplot as plt_ep6

from Episode_Script_Read import episode4_dict, episode5_dict, episode6_dict

print(episode5_dict.keys())


print("Episode 4 Characters and Number of Lines")
for key in episode4_dict.keys():
    print(key , ':', len(episode4_dict[key]), "Lines")
print("Episode 5 Characters and Number of Lines")
for key in episode5_dict.keys():
    print(key, ':', len(episode5_dict[key]), "Lines")
print("Episode 6 Characters and Number of Lines")
for key in episode6_dict.keys():
    print(key, ':', len(episode6_dict[key]), "Lines")

#The pie charts represent the characters in each movie who speak 6 or more lines for readability.

ep4_num_lines = []
ep4_chart_chars = []
for key in episode4_dict.keys():
    if len(episode4_dict[key]) > 5:
        ep4_num_lines.append(len(episode4_dict[key]))
        ep4_chart_chars.append(key)
fig4 = plt_ep4.figure(figsize = (25, 60))
plt_ep4.pie(ep4_num_lines, labels = ep4_chart_chars)
plt_ep4.show()
plt_ep4.savefig("ep4_num_char_lines_pie.png")

ep5_num_lines = []
ep5_chart_chars = []
for key in episode5_dict.keys():
    if len(episode5_dict[key]) > 5:
        ep5_num_lines.append(len(episode5_dict[key]))
        ep5_chart_chars.append(key)
fig5 = plt_ep5.figure(figsize = (25, 60))
plt_ep5.pie(ep5_num_lines, labels = ep5_chart_chars)
plt_ep5.show()
plt_ep5.savefig("ep5_num_char_lines_pie.png")

ep6_num_lines = []
ep6_chart_chars = []
for key in episode6_dict.keys():
    if len(episode6_dict[key]) > 5:
        ep6_num_lines.append(len(episode6_dict[key]))
        ep6_chart_chars.append(key)

fig6 = plt_ep6.figure(figsize = (25, 60))
plt_ep6.pie(ep6_num_lines, labels = ep6_chart_chars)
plt_ep6.show()
plt_ep6.savefig("ep6_num_char_lines_pie.png")
