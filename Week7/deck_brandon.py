from random import randint


SUIT_INDEX = 0
RANK_INDEX = 1


def make_deck(suits, card_values):
    result = []
    for suit in suits:
        for value in card_values:
            result.append([suit, value])
    return result


suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
card_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
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

    def hashable_list(deck):
        result = []
        for card in deck:
            result.append(card[SUIT_INDEX] + card[RANK_INDEX])
        return result

    hashable_test = hashable_list(test_deck)
    hashable_deck = hashable_list(DECK)

    assert len(set(hashable_test)) == 52
    assert len(set(hashable_deck)) == 52

    changed_position_count = 0
    for x in range(0, 52):
        if test_deck[x] != DECK[x]:
            changed_position_count += 1
    print (str(changed_position_count) + " cards changed position this shuffle.")

    def loop_test():
        loops = 0
        for x in range(0, 101):
            shuffle(DECK)
            loops += 1
        print ("Loops performed: " + str(loops))

    loop_test()


def decorate_cards(deck):
    result = []
    for card in deck:
        rank = numeral_to_string(card[RANK_INDEX])
        suit = card[SUIT_INDEX]
        decorated_card = rank + " of " + suit
        result.append(decorated_card)
    return result


def numeral_to_string(card_rank):
    numeral_ranks = {
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        '10': 'Ten',
    }
    if card_rank in numeral_ranks.keys():
        return numeral_ranks[card_rank]
    else:
        return card_rank


shuffled_deck = shuffle(DECK)

test_shuffle(shuffled_deck)

print ("Shuffled Deck:", decorate_cards(shuffled_deck))
