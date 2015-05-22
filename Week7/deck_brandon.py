# 52 elements

# e.g. [[hearts, king], [spades, 7], [clubs, jack]...]

from random import randint


def shuffle(input_list):
    deck = input_list
    cards_left = (len(deck)-1)
    random_int = randint(0, cards_left)

    result = []

    while cards_left:

        if deck[random_int] not in result:
            result.append(deck[random_int])
            deck = [x for x in deck if x not in result]
            cards_left = (len(deck)-1)
            random_int = randint(0, cards_left)
        else:
            random_int = randint(0, cards_left)

    return result

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
card_values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']


def make_deck(suits, card_values):
    result = []
    for suit in suits:
        for value in card_values:
            result.append([suit, value])
    return result

DECK = make_deck(suits, card_values)

print shuffle(DECK)





