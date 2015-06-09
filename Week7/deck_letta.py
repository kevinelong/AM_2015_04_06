__author__ = 'Letta'

# I did Tarot suits

import itertools, random

deck = list(itertools.product(range(1, 14), ['Wands', 'Cups', 'Swords', 'Coins']))
random.shuffle(deck)
<<<<<<< HEAD
print ("Your reading:")
=======
print("You got:")
>>>>>>> origin/master
for i in range(9):
    print(deck[i][0], 'of', deck[i][1])
