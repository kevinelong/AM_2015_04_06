__author__ = 'brandon'

game_state = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]


def draw():
    for row in game_state:
        line = []
        for column in row:
            line += column
        print line


# EXAMPLE OUTPUT
# O..
# .X.
# ...

game_state[1][1] = 'X'
game_state[0][0] = 'O'

draw()
