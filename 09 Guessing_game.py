import random

def guessingGame():
    a = random.randint(1,99)

    input = 0
    guess = 0

    while input!=a:
        input = int(input("Guess a number from 1 to 9\n\n"))
        guesses+=1

    print("You found it using ",guesses,"guess.")

guessingGame()
