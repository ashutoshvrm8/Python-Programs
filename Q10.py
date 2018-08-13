# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:53:41 2018

@author: Ashutosh Verma
"""

'''
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''

s = input()
words = [word for word in s.split(" ")]
print (" ".join(sorted(list(set(words)))))