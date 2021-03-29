# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 20:59:58 2019

@author: ouzij
"""


def list_all_links(s):
    s_list = []
    while 'a href' in s:
        a = s.find('a href=')
        begin_pos = a + 8
        x = begin_pos
        end_pos = s.find('"',x + 1)
        x1 = end_pos
        s1 = s[x:x1]
        print(s1)
        s_list.append(s1)
        s = s[x1:]
    return s_list
#webpage_source = input()
#return (list)
        
    