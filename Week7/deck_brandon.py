# 52 elements

# e.g. [[hearts, king], [spades, 7], [clubs, jack]...]

from random import randint


def make_deck(suits, card_values):
    result = []
    for suit in suits:
        for value in card_values:
            result.append([suit, value])
    return result


suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
card_values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
DECK = make_deck(suits, card_values)


def shuffle(input_list):
    deck = input_list
    cards_left = len(deck)
    cards_left_index = (cards_left - 1)
    random_int = randint(0, cards_left_index)
    result = []

    while cards_left:

        if deck[random_int] not in result:
            result.append(deck[random_int])
            deck = [x for x in deck if x not in result]
            cards_left = len(deck)
            cards_left_index = (cards_left-1)

            if cards_left:
                random_int = randint(0, cards_left_index)

    return result


def test_shuffle(test_deck):
    assert len(test_deck) == 52

    changed_position_count = 0
    for x in range(0, 52):
        if test_deck[x] != DECK[x]:
            changed_position_count += 1
    print changed_position_count, " cards changed position this shuffle."


shuffled_deck = shuffle(DECK)

test_shuffle(shuffled_deck)
print shuffled_deck

