game_state = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]


def draw():
    pass  # TODO PRINT GAME BOARD

    # working but inflexible example
    print(game_state[0][0], game_state[0][1], game_state[0][2])
    print(game_state[1][0], game_state[1][1], game_state[1][2])
    print(game_state[2][0], game_state[2][1], game_state[2][2])

# EXAMPLE OUTPUT
# O..
# .X.
# ...

game_state[1][1] = 'X'
game_state[0][0] = 'O'

draw()
