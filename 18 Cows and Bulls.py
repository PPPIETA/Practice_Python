import random

def game():
    number = str(random.choice(range(1000,9999)))
    guess = 0
    player = 0
    again = "y"
    result = {}
    print("Let's play a 'cow and bulls' game")
    while again not in "n":
        if len(str(player)) != 4:
            player = str(input("Give me a 4-digit number"))
        result = {"cows":0,"bulls":0}
        for el in range(len(str(number))):
            if number[el] == player[el]:
                result["cows"]+=1
            elif number[el] in player:
                result["bulls"]+=1
        print("You got {} cows and {} bulls!".format(result["cows"],result["bulls"]))
        if result["cows"]==4:
            break
        player = str(input("Give me a 4-digit number"))

    #again = str(input("Do you want to play again (y/n)")).lower()

if __name__=="__main__":
    game()
