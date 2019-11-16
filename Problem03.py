#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:33:40 2019

@author: dewiballard
"""

# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
# factor of the number 600851475143?

num = 13195
i=1

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

if num > 1: #not sure if needed, or whether this is different if while used
    for i in range(2,num):      #for every number from 1 to 13195
        if isprime(i) == True:      #is it a prime number?
            if (num % i) == 0:      #if yes, which are factors of 13195
                print(i)