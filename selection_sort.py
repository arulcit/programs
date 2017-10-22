#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:08:36 2017
selection sort
@author: Arul Perumal
"""

a = [54,26,93,17,77,31,44,55,20]
print a

list_length = len(a)

for i in xrange(list_length,1,-1):
    pos = 0
    found = False
    bign = 0
    for j in xrange(i):
        #check if current number is big? If so, update position and bignumber
        if a[j] > bign:
            pos = j
            bign = a[j]
            found = True
    if (found):
        a[pos],a[i-1] = a[i-1],a[pos]
    print a        

'''
output
[54, 26, 93, 17, 77, 31, 44, 55, 20]
[54, 26, 20, 17, 77, 31, 44, 55, 93]
[54, 26, 20, 17, 55, 31, 44, 77, 93]
[54, 26, 20, 17, 44, 31, 55, 77, 93]
[31, 26, 20, 17, 44, 54, 55, 77, 93]
[31, 26, 20, 17, 44, 54, 55, 77, 93]
[17, 26, 20, 31, 44, 54, 55, 77, 93]
[17, 20, 26, 31, 44, 54, 55, 77, 93]
[17, 20, 26, 31, 44, 54, 55, 77, 93]
'''
