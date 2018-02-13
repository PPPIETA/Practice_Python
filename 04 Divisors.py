# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:35:51 2017

@author: Hope
"""

number = int(input("Tell me your number\n"))
divisors = []
for n in range(1, number+1):
    if number%n ==0:
        divisors.append(n)

print(divisors)
