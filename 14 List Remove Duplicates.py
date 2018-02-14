a = [1,1,2,2,3,3,4,5,6,7,7,7,8,9,9,10,10]


def makeSet():
    b = []
    for num in a:
        if num not in b:
            b.append(num)
    print(b)

makeSet()
print(set(a))
