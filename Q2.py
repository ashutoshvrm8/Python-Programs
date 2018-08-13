# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 13:47:09 2018

@author: Ashutosh Verma
"""

'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
'''

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())

print (fact(x))