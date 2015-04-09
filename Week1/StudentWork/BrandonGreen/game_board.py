__author__ = 'brandon'

game_state = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]


def draw():
    for row in game_state:
        print row

    game_on = '.' in game_state
    turn = 1
    if turn % 2 == 0:
        whose_turn = 'Player 1'
    else:
        whose_turn = 'Player 2'

    #while game_on:


# EXAMPLE OUTPUT
# O..
# .X.
# ...

game_state[1][1] = 'X'
game_state[0][0] = 'O'

draw()

