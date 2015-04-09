game_state = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]

# PRINT GAME BOARD
def draw():
    for row in game_state:
        for piece in row:
            print(piece, end="")
        print()


# EXAMPLE OUTPUT
# O..
# .X.
# ...

game_state[1][1] = 'X'
game_state[0][0] = 'O'

draw()
