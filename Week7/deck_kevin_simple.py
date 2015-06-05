from random import random

deck = []
for s in range(0, 4):
    for n in range(1, 14):
        deck.append([s, n])

count = 0


def r(a):
    print(a)
    return random()


def spread(deck):
    suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
    rank = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

    for c in deck:
        print(rank[c[1] - 1], "of", suit[c[0]])


print(count)
spread(deck)
print("before:", deck)
deck.sort(key=r)
print("after:", deck)
# OUTPUT:
# ...
# 8 of Spades
# 9 of Spades
# 10 of Spades
# Jack of Spades
# Queen of Spades
# King of Spades
# Ace of Hearts
# 2 of Hearts
# ...
# before: [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [2, 12], [2, 13], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13]]
# after: [[2, 2], [0, 5], [3, 4], [3, 5], [3, 2], [0, 11], [2, 8], [2, 12], [2, 13], [2, 3], [2, 10], [3, 11], [1, 3], [3, 3], [2, 11], [1, 9], [0, 7], [3, 8], [0, 1], [2, 1], [2, 4], [3, 7], [3, 12], [0, 8], [3, 9], [0, 12], [1, 11], [1, 2], [2, 6], [0, 13], [0, 2], [0, 4], [3, 1], [0, 6], [1, 13], [1, 12], [0, 10], [0, 9], [1, 10], [1, 4], [1, 6], [3, 13], [2, 7], [3, 10], [1, 5], [0, 3], [1, 8], [1, 1], [2, 9], [3, 6], [2, 5], [1, 7]]