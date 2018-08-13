# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 14:05:19 2018

@author: Ashutosh Verma
"""

'''
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
'''

values=input()
l=values.split(",")
t=tuple(l)
print (l)
print (t)