#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:35:52 2019

@author: dewiballard
"""

# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder. What is the smallest positive number
# that is evenly divisible by all of the numbers from 1 to 20?

import datetime as dt

start = dt.datetime.now()

i = 0

while i < 100000000000000:
    i = i + 1
    if i % 20 == 0 and i % 19 == 0 and i % 18 == 0 and i % 17 == 0 and \
    i % 16 == 0 and i % 15 == 0 and i % 14 == 0 and i % 13 == 0 and \
    i % 12 == 0 and i % 11 == 0 and i % 10 == 0 and i % 9 == 0 and \
    i % 8 == 0 and i % 7 == 0 and i % 6 == 0 and i % 5 == 0 and \
    i % 4 == 0 and i % 3 == 0 and i % 2 == 0 and i % 1 == 0:
        print(i)
        break

end = dt.datetime.now()
print('This simulation took', end-start)

# THIS SOLUTION IS VERY SLOW. COME BACK TO IMPROVE