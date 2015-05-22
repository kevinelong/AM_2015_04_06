# 52 elements

# e.g. [[hearts, king], [spades, 7], [clubs, jack]...]

from random import randint

def shuffle(input_list):
    deck = input_list
    result = []

    for card in range(0, len(input_list)):
        cards_left = len(deck)
        random_int = randint(0, cards_left)

        if deck[random_int] not in result:
            deck.pop(random_int)
            result.append(deck[random_int])

    return result


suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
card_values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

def make_deck (suits, card_values):
    result = []
    for suit in suits:
        for value in card_values:
            result.append([suit, value])
    return result

DECK = make_deck(suits, card_values)

print shuffle(DECK)



