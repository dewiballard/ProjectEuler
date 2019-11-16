#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:42:29 2019

@author: dewiballard
"""

# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13. What is the 10 001st prime number?

i = 0
count = 0

def isprime(n):
# make sure n is a positive integer
    n = abs(int(n))
# 0 and 1 are not primes
    if n < 2:
        return False
# 2 is the only even prime number
    if n == 2:
        return True
# all other even numbers are not primes
    if not n & 1:
        return False
# range starts with 3 and only needs to go up the squareroot of n for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

for i in range(1,1000000):
    if isprime(i) == True:
        count = count + 1
        if count == 10001:
            print(i)
