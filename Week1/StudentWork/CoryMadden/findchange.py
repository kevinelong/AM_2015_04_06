__author__ = 'Cory'

change = {"nickels": 2,
          "dimes": 5,
          "quarters": 3}
total_change = float((change["nickels"] * 5) + (change["dimes"] * 10) + (change["quarters"] * 25))

print ("$" + str(total_change / 100))

# change["nickels"] = int(raw_input("How many nickels? "))
#
# total_change = float((change["nickels"] * 5) + (change["dimes"] * 10) + (change["quarters"] * 25))
#
# print ("$" + str(total_change / 100))