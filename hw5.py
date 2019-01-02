# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 22:18:28 2019

@author: Valeriy Rybalkin
"""
def isPrime(num):
    for count in range(2,int(num/2)+1):#Number must in range must be integer
    #There is no sense to get modulo to numbers greater then half of checked number
        if num%count == 0:#
            return False
    return True #if loop entirely was checked without returning False

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
    if(isPrime(count)):
        print("Prime")
        continue
    print(count)