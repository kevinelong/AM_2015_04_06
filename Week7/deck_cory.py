import random
import deck_brandon

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
    return deck

# players = []

def make_players(names):
    i = 0
    players = []
    while i < len(names):
        player = {'name': names[i],
                  'score': 0,
                  'hand': [],
                  }
        players.append(player)
        i += 1
    return players

def deal_cards(deck, players, hand_count):
    while len(players[len(players)-1]['hand']) < hand_count:
        i = 0
        for player in players:
            card = deck.pop(len(deck[len(deck)-1]))
            player['hand'].append(card)
            i += 1


if __name__ == '__main__':
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    card_values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    shuffle(deck_brandon.make_deck(suits, card_values), 20)
    names = ['Cory', 'Jack', 'Brandon', 'Danford', 'Brook', 'Sam', 'Letta', 'Kevin']
    players = make_players(names)
    deck = shuffle(deck_brandon.make_deck(suits, card_values), 20)
    deal_cards(deck, players, 5)
    print(players)