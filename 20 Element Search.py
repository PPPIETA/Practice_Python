import random

def binary():
    a = sorted(random.sample(range(100),100))
    number = int(input("Give me a number from 0 to 100\n\n"))
    calculate = True
    while calculate:
        print(a)
        if number != a[0] and len(a) == 1:
            print("It's not in the list")
            calculate = False
        elif number < a[len(a)//2]:
            a = a[:len(a)//2]
        elif number > a[len(a)//2]:
            a = a[len(a)//2:]
        elif number == a[0] or number == a[1]:
            print("It's in the list")
            calculate = False
        else:
            a=a.pop()

binary()
