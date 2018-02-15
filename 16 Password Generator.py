import random
import string

def generatePassword():
    length = int(input("How long password you need?\n"))

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    allOptions = letters+numbers+symbols
    password = ""

    for el in range(length):
        password+=random.choice(allOptions)
    print(password)

generatePassword()
