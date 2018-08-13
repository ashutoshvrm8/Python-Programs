# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:43:08 2018

@author: Ashutosh Verma
"""

'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

items=[x for x in input().split(',')]
items.sort()
print (','.join(items))