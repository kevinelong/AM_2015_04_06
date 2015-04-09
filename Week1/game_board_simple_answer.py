game_state = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]


def draw():
    pass  # TODO PRINT GAME BOARD

    # working but inflexible example
    # print(game_state[0][0], game_state[0][1], game_state[0][2])
    # print(game_state[1][0], game_state[1][1], game_state[1][2])
    # print(game_state[2][0], game_state[2][1], game_state[2][2])

    #FIVE LINES
    for row in game_state:
        line = ''
        for column in row:
            line += column
        print(line)

    #With buffered output
    output = ""
    for row in game_state:
        line = ''
        for column in row:
            line += column
        output = output + line + "\n"
    print(output)

    # With buffered output and using join,
    #  so as to be fast and memory efficient.
    lines = []
    for row in game_state:
        line = ''
        for column in row:
            line += column
        lines.append(line)
    output = "\n".join(lines)
    print(output)

    # output = ""
    # index = 0
    # for row in game_state:
    #     for column in row:
    #         output = output + column
    #         index = index + 1
    #         if ((index % len(game_state)) == 0):
    #             output = output + "\n"
    # print(output)

# EXAMPLE OUTPUT
# O..
# .X.
# ...

game_state[1][1] = 'X'
game_state[0][0] = 'O'

draw()
