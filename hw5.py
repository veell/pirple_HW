# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 22:18:28 2019

@author: Admin
"""

for count in range(1,101):
    if (count%3 == 0) and (count%5 == 0):
        print("FizzBuzz")
        continue
    if count%3 == 0:
        print("Fizz")
        continue
    elif count%5 == 0:
        print("Buzz")
        continue
    print(count)