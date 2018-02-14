def giveNumber(text="Give me number and I will check if it's Prime"):
    return int(input(text))

def checkDivisor(number,div):
    if number%div==0:
        return True

def isPrime():
    number = giveNumber()
    divisors = []

    for num in range(2,number-1):
        if checkDivisor(number,num)==True:
            divisors.append(num)

    if len(divisors)>0:
        print("This is no Prime!!!")
    else:
        print("This is Prime!!!")

isPrime()
