# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:35:51 2017

@author: Hope
"""

word = input("Tell me a Palindrome word?\n\n")

def isPalindrome(word):
    for letter in range(len(word)):
        if word[0] != word[(-1)]:
            print("This ain't no Palindrome\n")
            break
        else:
            try: word = word[1:-1]
            except IndexError:
                continue
            finally:
                print("Yes %s is a Palindrome\n" % word)

def palindrome(word):
    if word==word[::-1]:
        print("Yes it's a Palindrome")
    else:
        print("This is no Palindrome")

isPalindrome(word)
