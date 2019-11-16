#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:41:26 2019

@author: dewiballard
"""

# Problem 6
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

sumsquare = 0
count = 0

for i in range(0,101):
    square = i**2
    sumsquare = sumsquare + square

for i in range(0,101):
    i = i
    count = count + i
    countsquare = count**2

difference = countsquare - sumsquare
print(difference)
