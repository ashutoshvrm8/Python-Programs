# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 13:50:43 2018

@author: Ashutosh Verma
"""

'''
Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
'''

n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print (d)