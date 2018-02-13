# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:35:51 2017

@author: Hope
"""

lista = [1, 77, 1, 2, 3, 5, 8, 13, 1, 21, 34, 55, 89, 4]

nowa = []

for n in lista:
    if n<5:
        nowa.append(n)

print(nowa)

max = int(input("Give me max number for list\n\n"))

print([n for n in lista if n<max])
