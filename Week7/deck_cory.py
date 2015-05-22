import random


def shuffle(deck, loop):
    i = 0
    loop_count = 0
    while loop_count < loop:
        while i < len(deck):
            index = random.randint(0, len(deck) - 1)
            hold = deck[index]
            deck[index] = deck[i]
            deck[i] = hold
            i += 1
        loop_count += 1
    print(deck)


def make_deck(suits, card_values):
    result = []
    for suit in suits:
        for value in card_values:
            result.append([suit, value])
    return result


if __name__ == '__main__':
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    card_values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    shuffle(make_deck(suits, card_values), 5)
