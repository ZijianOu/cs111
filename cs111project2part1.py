# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:39:14 2019

@author: ouzij
"""

def print_all_links(s):
    while 'a href' in s:
        first_a = s.find('a href=')
        begin_pos = first_a+8
        x = begin_pos
        end_pos = s.find('"',x+1)
        x1 = end_pos
        s1 = s[x:x1]
        print(s1)
        s = s[x1:]
webpage_source = input()
print_all_links(webpage_source)
