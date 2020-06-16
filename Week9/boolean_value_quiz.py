import random
import sys

bools = {
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

if sys.version_info<(3,0):
    def input(parameter):
        return raw_input(parameter)
else:
    pass


def random_question():
    global bools
    question = random.choice(list(bools))
    answer = bools[question]

    return question, answer


def game():
    global bools, SCORE
    questions_asked = 0
    total_questions = len(bools)
    print('Welcome to the boolean value game!\nType True or False for each question.')
    while questions_asked <= total_questions:
        left = len(bools)
        print("You have answered %d of %d questions correctly." % (SCORE, questions_asked))
        print("There are %d questions left." % (total_questions-questions_asked))
        question = random_question()
        player_answer = input("What is the value of %s?: " % question[0])
        if player_answer.upper() == str(question[1]).upper():
            print("That is correct!")
            del bools[question[0]]
            SCORE += 1
        else:
            print("Sorry, that is not correct.")
        questions_asked += 1

game()