#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:45:45 2019

@author: dewiballard
"""

# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all
# the primes below two million.

total = 0

i = 1

def isprime(n):
    '''check if integer n is a prime'''
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
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

for i in range(1, 2000000):
    if isprime(i) == True:
        total = total + i
        print(total)
