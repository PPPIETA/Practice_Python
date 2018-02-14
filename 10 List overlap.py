import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = random.sample(range(100),30)
d = random.sample(range(100),30)

print([x for x in set(a) if x in set(b)])
print([x for x in set(c) if x in set(d)])
