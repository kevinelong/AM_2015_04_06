from random import random

deck = []
for s in range(0, 4):
    for n in range(1, 14):
        deck.append([s, n])

print("before:", deck)


def r(a):
    return random()


deck.sort(key=r)
print("after:", deck)