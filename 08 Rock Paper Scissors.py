# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:35:51 2017

@author: Hope
"""

def playMe():
    wannaplay = "y"
    win = ""
    lose = ""
    tie = ""

    while wannaplay not in "n":
        play1 = str(input("P1: Choose Rock - Paper - Scissors (r/p/s)\n")).lower()
        play2 = str(input("P2: Choose Rock - Paper - Scissors (r/p/s)\n")).lower()

        print("Let's Play -> First player\n")

        while play1 not in "rps":#("r"or"p"or"s"):
            play1 = str(input("P1: Choose Rock - Paper - Scissors (r/p/s)\n")).lower()

        print("Now it's your turn -> Second player\n")
        while play2 not in "rps":#("r"or"p"or"s"):
            play2 = str(input("P2: Choose Rock - Paper - Scissors (r/p/s)\n")).lower()

        if play1 == "r":
            win = "s"
            lose = "p"
            tie = "r"
        elif play1 == "s":
            win = "p"
            lose = "r"
            tie = "s"
        else:
            win = "r"
            lose = "s"
            tie = "p"

        if play2==win:
            print("Player1 wins!!!\n")
        elif play2==lose:
            print("Player2 wins!!!\n")
        else:
            print("It's a tie!!!\n")
        wannaplay = str(input("Do you want to play (y/n)\n")).lower()

playMe()
