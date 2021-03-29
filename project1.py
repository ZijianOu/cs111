# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:05:42 2019

@author: ouzij
"""
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#def rotate(a, num):
#    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#    index = alphabet.find(a)
#   return alphabet[(index + num)%26]
def c_encrypt(string, num):
    string = string.upper()
    newstring = ''
    for i in string:
        if i in alphabet:
            #r = rotate(i, num)
            index1 = alphabet.find(i)
            index2 = (index1 + num)%26
            newstring += (alphabet[index2])
        else:
            newstring += i
    print (newstring)
    return newstring

    
def c_decrypt(string, num):
    string = string.upper()
    newstring = ''
    for i in string:
        if i in alphabet:
            index1 = alphabet.find(i)
            index2 = (index1 + 26 - num)%26
            newstring += (alphabet[index2])
        else:
            newstring += i
        print (newstring)
    return newstring

def vig_encrypt(string1, string2):
    string1 = string1.upper()
    string2 = string2.upper()
    new_string1 = ''
    counter = 0
    for c in string1:
        if counter >= len(string2):
            counter = 0
        if c in alphabet:
            index1 = alphabet.find(string2[counter])
            index2 = alphabet.find(c)
            index3 = (index1 + index2)%26
            counter += 1
            new_string1 += (alphabet[index3])
        else:
            new_string1 += c
    return new_string1
print(vig_encrypt('abz', "ABZ"))
    
def vig_decrypt(string1, string2):
    string1 = string1.upper()
    string2 = string2.upper()
    new_string1 = ''
    counter = 0
    for c in string1:
        if counter >= len(string2):
            counter = 0
        if c in alphabet:
            index1 = alphabet.find(string2[counter])
            index2 = alphabet.find(c)
            index3 = (index2 - index1)%26
            counter += 1
            new_string1 += (alphabet[index3])
        else:
            new_string1 += c
    return new_string1
print(vig_encrypt('Hi Mom!', 'LEMON'))