#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:35:08 2019

@author: dewiballard
"""

# Problem 4
# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

limit = 999*999
i = 0

while i < limit:
    i = i + 1
    if str(i) == str(i)[::-1]:
        for m in range(100, 999):
                if i % m == 0 and 100 < i / m <= 999:
                    print(i)
