
def howLong():
    return int(input("How long Fibonacci you want?"))

def fibo():
    fib = [1,1]

    long = howLong()
    if long == 1:
        print([fib[0]])
    else:
        for num in range(2,long):
            fib.append(fib[num-1]+fib[num-2])

        print(fib)

fibo()
