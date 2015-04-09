# tic tac toe


class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.value = "."


class Board:
    def __init__(self, size):
        self.size = size
        self.clear_board()

    def clear_board(self):
        self.positions = []
        for row_index in range(0, self.size):
            row = []
            for column_index in range(0, self.size):
                row.append(Position(row_index, column_index))
            self.positions.append(row)

    def draw(self):
        lines = []
        header = " "
        for c in range(1, self.size + 1):
            header += str(c)
        header = " ".join(header)
        row_index = 1
        lines.append(header)
        for row in self.positions:
            line = ""
            line += str(row_index)
            for column in row:
                line += column.value
            row_index += 1
            lines.append(" ".join(line))
        lines.append("-" * (2 * self.size + 1))
        print("\n".join(lines))

    def add(self, move):
        if move.x < self.size and move.y < self.size and move.x >= 0 and move.y >= 0:
            self.positions[move.x][move.y].value = move.value
            return True
        else:
            return False

    def clear_position(self, move):
        self.current_state[move.x][move.y] = move.value


class Move:
    valid = True
    parts = []
    x = -1
    y = -1
    value = "."
    errors = []

    def __init__(self, raw, player):
        self.valid = True
        self.errors = []
        self.value = player.value
        self.parse(raw)

    def parse(self, raw):
        self.parts = raw.split(",")
        self.validate()
        if self.valid:
            self.x = int(self.parts[0]) - 1
            self.y = int(self.parts[1]) - 1

    def validate(self):
        if not (2 == len(self.parts)):
            self.errors.append("Moves must have two coordinates.")
        else:
            x = self.parts[0]
            y = self.parts[1]

            if (not x.isdigit()) or (not y.isdigit()):
                self.errors.append("Moves must be in the form x,y e.g. 1,1")

        if len(self.errors) > 0:
            self.valid = False


class Player:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Game:
    user_input = ""
    prompt = "%s, '%s' enter x,y or quit. e.g. 1,1:  "
    moves = []

    def __init__(self, player_list=[], size=3, goal=3):
        self.goal = goal
        self.board = Board(size)
        self.players = player_list
        self.current_index = 0

    def play_game(self):
        self.playing_game = True
        while self.playing_game:
            self.get_input()
            self.process_input()
        self.close_game("Good Bye!")

    def get_current_player(self):
        return self.players[self.current_index]

    def display_state(self):
        self.board.draw()

    def get_input(self):
        self.user_input = input(self.prompt % (self.get_current_player().name, self.get_current_player().value))

    def next_player(self):
        self.current_index += 1
        if self.current_index >= len(self.players):
            # return to beginning
            self.current_index = 0

    def is_empty(self, move):
        if (self.board.positions[move.x][move.y].value == "."):
            return True
        else:
            move.errors.append("not empty")
            return False

    def is_move_on_board(self, move):
        if move.x >= self.board.size or move.x < 0:
            move.errors.append("Move x is off of board")
        if move.y >= self.board.size or move.y < 0:
            move.errors.append("Move y is off of board")
        if len(move.errors) > 0:
            move.valid = False
        else:
            move.valid = True
        return move.valid

    def apply_move(self, move):
        self.moves.append(move)
        self.board.add(move)
        # if not self.board.check_win()
        self.board.draw()
        self.next_player()

    def print_errors(self, move):
        print("Error(s):")
        print(" ".join(move.errors))

    def process_input(self):

        if self.user_input == "quit":
            self.playing_game = False
        else:
            move = Move(self.user_input, self.get_current_player())
            if move.valid and self.is_move_on_board(move) and self.is_empty(move):
                self.apply_move(move)
            else:
                self.print_errors(move)

    def close_game(self, closing_message):

        print(closing_message)


players = []
players.append(Player('Player One', 'X'))
players.append(Player('Player Two', 'O'))
players.append(Player('Player Three', 'Z'))

board_size = 9
goal_in_a_row = 5
games_instance = Game(players, board_size, goal_in_a_row)
games_instance.play_game()

# example output
# Player Three, 'Z' enter x,y or quit. e.g. 1,1:  6,6
#   1 2 3 4 5 6 7 8 9
# 1 X . . . . . . . .
# 2 . . . . . . . . .
# 3 . . . . . . . . .
# 4 . . . . . . . . .
# 5 . . . . . . . . .
# 6 . . . . . Z . . .
# 7 . . . . . . . . .
# 8 . . . . . . . . .
# 9 . . . . . . . . O
# -------------------