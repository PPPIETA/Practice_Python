import random

a = random.sample(range(100),10)

print([x for x in [a.pop(0),a.pop()]])
