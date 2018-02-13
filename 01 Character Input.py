# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:35:51 2017

@author: Hope
"""

import datetime

now = datetime.datetime.now()

name = input("Tell me your name, please?\n\n")
age = int(input("Tell me your age, please?\n\n"))
many = int(input("Tell me how many times I should print result?\n\n"))
year = str(now.year-age+100)
result = "Hello "+name+", You will turn 100yo in "+year

if many > 0:
    print(result*many)
else:
    print(result)

quit = input("do you want to quit?\n\n")
