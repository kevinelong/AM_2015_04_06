import random

boolean_expressions = {
    'not False': not False,
    'not True': not True,
    'True or False': True or False,
    'True or True': True or True,
    'False or True': False or True,
    'False or False': False or False,
    'True and False': True and False,
    'True and True': True and True,
    'False and True': False and True,
    'False and False': False and False,
    'not (True or False)': not (True or False),
    'not (True or True)': not (True or True),
    'not (False or True)': not (False or True),
    'not (False or False)': not (False or False),
    'not (True and False)': not (True and False),
    'not (True and True)': not (True and True),
    'not (False and True)': not (False and True),
    'not (False and False)': not (False and False),
    '1 != 0': 1 != 0,
    '1 != 1': 1 != 1,
    '0 != 1': 0 != 1,
    '0 != 0': 0 != 0,
    '1 == 0': 1 == 0,
    '1 == 1': 1 == 1,
    '0 == 1': 0 == 1,
    '0 == 0': 0 == 0,
}

SCORE = 0


def random_question():
    global boolean_expressions
    question = random.choice(list(boolean_expressions.keys()))
    answer = boolean_expressions[question]

    return question, answer


def game():
    global boolean_expressions, SCORE
    print('Welcome to the boolean value game!')
    print('Type True or False for each question.')
    length = len(boolean_expressions)
    while len(boolean_expressions) > 0:
        left = len(boolean_expressions)
        print("You have answered {0} of {1} questions correctly.".format(SCORE, length))
        print("There are %d questions left." % left)
        question = random_question()
        player_answer = input("What is the value of {0}?: ".format(question[0]))

        if player_answer == str(question[1]):
            print("That is correct!")
            del boolean_expressions[question[0]]
            SCORE += 1
        else:
            print('Incorrect.')
    print("FINAL SCORE: {0} of {1} questions".format(SCORE, length))


game()