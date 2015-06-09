# x = 6
# total = 10 * x
# print total
#
# x = 45
# total = 42 / x
# print total
#
# x = 749
# total = 972 * x
# print total
#
# print(len("I am really tired"))
#
# print(len("Today is the day."))
#
# for person in ["Jade", "Margot", "Alexa", "Miranda"]:
#     print (person)
#
# data =[
#     { "name": "Miranda" },
#
#     {"name": "Alexa" }]
#
# key_field = "name"
# output = {}
#
# for item in data:
#      values = []
#      output_key = ""
#
#      for k in item.keys():
#          if k == key_field:
#              output_key = item[k]
#          else:
#              values.append(item[k])
#          output[output_key] = values
#
# print (output)

#Guess the number

import random

guessesTaken = 0

print ('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well,' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.' ) #There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') #There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high!')

    if guess == number:
        break

if guess == number:
        guessesTaken == str(guessesTaken)
        print('Good job, ' + myName + ' ! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
str(guessesTaken)
