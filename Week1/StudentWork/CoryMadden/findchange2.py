__author__ = 'Cory'

change = {"nickels":[2,5],
          "dimes": [5,10],
          "quarters": [3,25]}

QUANTITY = 0
VALUE = 1

total = 0

for coin in change:
    total += float(change[coin][QUANTITY]*change[coin][VALUE])

print("$" + str(total/100))