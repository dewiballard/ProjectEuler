#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:53:12 2019

@author: dewiballard
"""

# Problem 19
# Number of Sundays falling on 1st day of month between 1901 and 2000.

import datetime as dt
import bisect

import datetime as dt

start = datetime.datetime.now()
  
###########################################################################

jan_1_1901 = dt.date(1901, 1, 1)
dec_31_2000 = dt.date(2000, 12, 1)
sundays = []

while jan_1_1901 < dec_31_2000:
    if jan_1_1901.month+1 >= 13:
        jan_1_1901 = dt.date(jan_1_1901.year+1, 1, 1)
        if jan_1_1901.weekday() == 6:
            sundays.append(jan_1_1901)
    else:
        jan_1_1901 = dt.date(jan_1_1901.year, jan_1_1901.month+1, 1)
        if jan_1_1901.weekday() == 6:
            sundays.append(jan_1_1901)
   
print(len(sundays))

###########################################################################
end = datetime.datetime.now()

runtime = end - start
print('Simulation run time', runtime)
