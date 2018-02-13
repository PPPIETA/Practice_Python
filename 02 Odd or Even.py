# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:35:51 2017

@author: Hope
"""

number = int(input("Tell me a number\n\n"))
div = int(input("Tell me number you want to divide by\n\n"))

if number%4==0:
    print("Your number is divisible by 4")
elif number%2==0:
    print("Your number is even")
else:
    print("Your number is odd")

if number%div==0:
    print(str(num)+"is divisible by "+str(div))
else:
    print(str(num)+"is not divisible by "+str(div))
