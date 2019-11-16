#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:48:12 2019

@author: dewiballard
"""

# Problem 12
# Code works for smaller numbers, but doesn't scale well at all.

import time
start = time.time()

a=0
b=0

# This function gives the number of factors the number x has
#def nfactors(x):
#    numberoffactors = []
#    for i in range(1, x + 1):
#        if x % i == 0:
#            numberoffactors.append(i)
#            if len(numberoffactors) >= 50:
#                return True
            
#while b < 100000000:
#    a = a+1
#    b = b+a
#    if nfactors(b) == True:
#        print(b)
#        break

for i in range(1, 10000):
    nfactors = [i]
    for x in range(1, i):
        if i % x == 0:
            nfactors.append(x)
            if len(nfactors) >= 50:
                print(nfactors)

end = time.time()

elapsed = end - start

print(elapsed)
