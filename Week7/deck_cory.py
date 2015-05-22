import random

def shuffle(deck, loop):
    i = 0
    loop_count = 0
    while loop_count < loop:
        while i < len(deck):
            index = random.randint(0, len(deck)-1)
            hold = deck[index]
            deck[index] = deck[i]
            deck[i] = hold
            i += 1
        loop_count += 1
    print(deck)


if __name__ == '__main__':
    # deck = []
    deck = [
        {1: {
            'suit': 'Spades',
            'value': 'Ace',
        }
        },
        {2: {
            'suit': 'Spades',
            'value': 2,
        }
        },
        {3: {
            'suit': 'Spades',
            'value': 3,
        }
        },
        {4: {
            'suit': 'Spades',
            'value': 4,
        }
        },
        {5: {
            'suit': 'Spades',
            'value': 5,
        }
        },
        {6: {
            'suit': 'Spades',
            'value': 6,
        }
        },
        {7: {
            'suit': 'Spades',
            'value': 7,
        }
        },
        {8: {
            'suit': 'Spades',
            'value': 8,
        }
        },
        {9: {
            'suit': 'Spades',
            'value': 9,
        }
        },
        {10: {
            'suit': 'Spades',
            'value': 10,
        }
        },
        {11: {
            'suit': 'Spades',
            'value': 10,
        }
        },
        {12: {
            'suit': 'Spades',
            'value': 10,
        }
        },
        {13: {
            'suit': 'Spades',
            'value': 10,
        }
        },
        {14: {
            'suit': 'Clubs',
            'value': 'Ace',
        }
        },
        {15: {
            'suit': 'Clubs',
            'value': 2,
        }
        },
        {16: {
            'suit': 'Clubs',
            'value': 3,
        }
        },
        {17: {
            'suit': 'Clubs',
            'value': 4,
        }
        },
        {18: {
            'suit': 'Clubs',
            'value': 5,
        }
        },
        {19: {
            'suit': 'Clubs',
            'value': 6,
        }
        },
        {20: {
            'suit': 'Clubs',
            'value': 7,
        }
        },
        {21: {
            'suit': 'Clubs',
            'value': 8,
        }
        },
        {22: {
            'suit': 'Clubs',
            'value': 9,
        }
        },
        {23: {
            'suit': 'Clubs',
            'value': 10,
        }
        },
        {24: {
            'suit': 'Clubs',
            'value': 10,
        }
        },
        {25: {
            'suit': 'Clubs',
            'value': 10,
        }
        },
        {26: {
            'suit': 'Clubs',
            'value': 10,
        }
        },
        {27: {
            'suit': 'Hearts',
            'value': 'Ace',
        }
        },
        {28: {
            'suit': 'Hearts',
            'value': 2,
        }
        },
        {29: {
            'suit': 'Hearts',
            'value': 3,
        }
        },
        {30: {
            'suit': 'Hearts',
            'value': 4,
        }
        },
        {31: {
            'suit': 'Hearts',
            'value': 5,
        }
        },
        {32: {
            'suit': 'Hearts',
            'value': 6,
        }
        },
        {33: {
            'suit': 'Hearts',
            'value': 7,
        }
        },
        {34: {
            'suit': 'Hearts',
            'value': 8,
        }
        },
        {35: {
            'suit': 'Hearts',
            'value': 9,
        }
        },
        {36: {
            'suit': 'Hearts',
            'value': 10,
        }
        },
        {37: {
            'suit': 'Hearts',
            'value': 10,
        }
        },
        {38: {
            'suit': 'Hearts',
            'value': 10,
        }
        },
        {39: {
            'suit': 'Hearts',
            'value': 10,
        }
        },

    ]
    shuffle(deck, 5)
