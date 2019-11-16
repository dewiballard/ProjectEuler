#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:44:45 2019

@author: dewiballard
"""


# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

target = 1000

a =[i for i in range(target)]

for x in a:
    for y in range(target-x):
        z = target - x - y
        if x*x + y*y == z*z:
            if x > 0 and y > 0 and z > 0:
                print(x, y, z)
                print(x*y*z)
