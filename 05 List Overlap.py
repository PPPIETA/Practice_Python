# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:35:51 2017

@author: Hope
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print([x for x in set(a) if x in set(b)])
