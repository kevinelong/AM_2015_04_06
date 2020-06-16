# for x in fruit
#     print (x)
#
#     X = 0
#
# while x <= 100:
#     x = 0
#     print x += 1
#
# numbers = range(1, 101)
# print numbers
#
# numbers = range (1, 101, 2)
# print numbers
# #range, will count by twos
#
# word1 = 'Hello'
# word2 = 'World'
# print word1 + '' + word2
# #concatination
# x = 1
# y = raw_input('Enter a letter: ')
# print word1 * 10
#
# print word1 [x::2]
#
# print word1.lower()
#
# print y.lower() in word1.lower()

#*try and except
# try:
#     choice = int(raw_input("Enter a number:"))
#     if choice == 1:
#         print 'Yay'
#     else:
#         print 'NOOOOoooo...'
# except ValueError:
#     print 'That is not a number!'
#
# #*classes - the class has the components to make the thing
#
# class BankAccount():
#     def __init__(self, acct_name):
#         self.balance = 0
#         self.acct_name = acct_name
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
#
# chris = BankAccount ("Chris' Account")
# #variable class string
# print chris.balance
# print chris.acct_name
#
# chris.deposit(1000)
# print chris.balance
# chris.balance = 1000000000
# print chris.balance
#
# #inheirtance
#
# class MinimumBalanceAccount(BankAccount):
#     def __init__(self, minimum_balance):
#         BankAccount.__init__(self)
#         self.minimum_balance = minimum_balance
#
#     def withdraw(self, amount):
#         if self.balance - amount < self.minimum_balance:
#             print 'Sorry, minimum balance must be maintained.'
#         else:
#             BankAccount.withdraw(self, amount,)
#
# sally =BankAccount()
# chris = MinimumBalanceAccount(100)
# sally.deposit(150)
# chris.deposit(150)
# print sally.balance
# print chris.balance
# sally.withdraw(75)
# chris.withdraw(75)
# print chris.balance
# print sally.balance

'''
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble
if they are both smiling or if neither of them is smiling. Print True if we are in trouble.
'''

# def monkey_trouble(a_smile, b_smile):
#     if a_smile and b_smile:
#         return True
#     elif not a_smile and not b_smile:
#         return True
#     else:
#         print False

# def monkey_trouble(a_smile, b_smile):
#     print (a_smile == b_smile)
# monkey_trouble(True, True) #True
# monkey_trouble(False, False) #True
# monkey_trouble(True, False) #False


'''Given 3 int values, abc, return their sum. However, if one of the values is 13 then it does not count toward the sum
and values to its right do not count. So for example, if b is 13, then both b and c do not count.'''

# def lucky_sum(a,b,c):
#     list = [a, b, c]
#     sum = 0
#     if 13 in list:
#         i =list.index(13)
#         for x in list[:i]:
#             sum +=x
#
#     else:
#         sum = a + b + c
#     return sum
#
#     lucky_sum(1, 2, 3) #6
#     lucky_sum(1, 2, 13) #3
#     lucky_sum(1, 13, 3) #1

#*my answer, haha
# lucky_sum = 1 + 2 + 3
# print lucky_sum
# lucky_sum = 1 + 2 / 13
# print lucky_sum
# lucky_sum = 1 /13 + 3
# print lucky_sum

'''Given 3 int values, a b c, return their sum. However, if any of the values is a teen --- in the range 13...19
inclusive -- then that teen counts as 0, except 15 and 16 do not count as teens. Write a seperate helper
"def fix_teen(n):" that takes in int value and returns that value fixed for the teen rule. In this way, you avoid
reapeating the teen code 3 times (i.e. "decompisition"). Define the helper below and at the same indent level as the
main no_teen_sum.'''

def no_teen_sum(a, b, c):
    pass
no_teen_sum(1, 2, 3) #6
no_teen_sum(2, 13, 1) #3
no_teen_sum(2, 1, 14) #3

def no_teen_sum(a, b, c):
    list = [a, b, c]
    sum = 0
    if ([13, 14, 17, 18, 19]) in list:
        i =list.index(13, 14, 15, 17, 18, 19)
        for x in list[:i]:
            sum +=x
    else:
        sum = a + b + c
    return sum
print no_teen_sum