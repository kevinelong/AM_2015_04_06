# __author__ = 'Cory'
#
# fruit = ['apple','grape']
#
# for x in fruit:
# print (x)
#
# x = 0
#
# while x <= 100:
#     print x
#     x += 1
#
# numbers = range(1,101,4)
#
# print numbers
#
# words = 'Hello World'
#
# word1 = 'Hello'
# word2 = 'World'
#
# print word1 + ' ' + word2
#
# # word1[start,end,step]
# print word1[0:-1:2]
#
#
#
# try:
#     choice = int(raw_input("Enter a number: "))
#     if choice == 1:
#         print 'Yay!'
#     else:
#         print 'Nooooooooooooo!'
# except ValueError:
#     print "That's not a number."

#
# def deposit(amount):
#     global balance
#     balance += amount
#     return balance
#
# def withdraw(amount):
#     global balance
#     balance -= amount
#     return balance
#
# class BankAccount():
#     def __init__(self):
#         self.balance = 0
#         # self.acct_name = acct_name
#
#     def withdraw(self, amount):
#         self.balance -= amount
#         return self.balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def __str__(self):
#         return self.acct_name
#
#
#
# Cory = BankAccount(raw_input("Account name: "))
# print Cory.balance
# Cory.withdraw(int(raw_input("How much to take out: ")))
# print Cory.balance
# print Cory.acct_name
# print Cory
#
# user_list = []
#
# user_list.append(BankAccount(raw_input("Name of account owner: ")))
# user_key = len(user_list)
# print user_list[user_key]

# class MinimumBalanceAccount(BankAccount):
#     def __init__(self, minimum_balance):
#         BankAccount.__init__(self)
#         self.minimum_balance = minimum_balance
#
#     def withdraw(self, amount):
#         if self.balance - amount < self.minimum_balance:
#             print "Sorry, insufficient funds to maintain min."
#         else:
#             BankAccount.withdraw(self, amount)
#
#
# Sally = BankAccount()
# Chris = MinimumBalanceAccount(100)
# Sally.deposit(150)
# Chris.deposit(150)
#
# print Sally.balance
# print Chris.balance
#
# Sally.withdraw(75)
# Chris.withdraw(75)
#
# print Sally.balance
# print Chris.balance
#
# def lucky_sum(a,b,c):
#     total = a + b + c
#     if a == 13:
#         total -= 13
#     elif b == 13:
#         total -= 13
#     elif c == 13:
#         total -= 13
#     return total
#
# print lucky_sum(1,2,3)
# print lucky_sum(1,2,13)
# print lucky_sum(1,13,3)
#
# def lucky_sum2(a,b,c):
#     sum_2 = 0
#     list = [a,b,c]
#     for number in list:
#         if number != 13:
#             sum_2 += number
#         else:
#             break
#     return sum_2
#
# lucky_numbers = 1,13,3
#
# print lucky_sum2(1,13,6)
#
teen_range = range(12,20)
def fix_teen(number):
    if number == 15:
        return number
    elif number ==16:
        return number
    else:
        return 0

def no_teen_sum(a,b,c):
    list = [a,b,c]
    total = 0
    for number in list:
        if number in teen_range:
            number = fix_teen(number)
            total += number
        else:
            total += number
    return total

print no_teen_sum(1,2,3)
print no_teen_sum(2,13,1)
print no_teen_sum(2,1,14)
print no_teen_sum(2,15,1)