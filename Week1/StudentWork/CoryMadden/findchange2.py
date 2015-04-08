__author__ = 'Cory'

change = {"nickels":[2,5],
          "dimes": [5,10],
          "quarters": [3,25]}

coin_list = []
QUANTITY = 0
VALUE = 1

total = 0

for coin in change.keys():
    total += float(change[coin][QUANTITY]*change[coin][VALUE])
    # print (coin + " : " + str(change[coin][QUANTITY]) + " = $" + str(((float(change[coin][QUANTITY]*change[coin][VALUE]))/100)))
    coin_list.append(coin + " : " + str(change[coin][QUANTITY]) + " = $" + str(((float(change[coin][QUANTITY]*change[coin][VALUE]))/100)))
print("$" + str(total/100))
print coin_list