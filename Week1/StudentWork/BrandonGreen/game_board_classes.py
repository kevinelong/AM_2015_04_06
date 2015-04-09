__author__ = 'brandon'


class GameSquare():
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.value = '.'


class Player():
    def __init__(self, name, game_piece):
        self.name = name
        self.game_piece = game_piece


class Board():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def create_board(self):
        new_board = []
        for row in range(0, self.rows):
            line = []
            for column in range(0, self.columns):
                line.append(GameSquare(row, column).value)
            new_board.append(line)
        return new_board


def draw():
    for row in my_game:
        line = ''
        for column in row:
            line += column
        print line


def game_on(board):
    game_over = False
    turn = 0
    while not game_over:


my_board = Board(3, 3)
my_game = my_board.create_board()

draw()

