__author__ = 'brandon'

game_state = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]


def draw():
    for row in game_state:
        line = []
        line_item = ''
        for column in row:
            line.append(column)
        for item in line:
            line_item += item
        print(line_item)

# EXAMPLE OUTPUT
# O..
# .X.
# ...

game_state[1][1] = 'X'
game_state[0][0] = 'O'

draw()
