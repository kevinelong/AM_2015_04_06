__author__ = 'Sam Baron'


class Position(object):
    """
        Position on Board

        Properties:
            Row - cannot be larger than board rows
            Column - cannot be larger than board columns
            Symbol - position's symbol

        Methods:
            Set Position Value - using player's symbol
            Clear Position Value - setting position to board blank symbol
    """

    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value


class Board(object):
    """
        Game Board

        Properties:
            Rows
            Columns
            Blank Symbol to clear board
            Position Dictionary

        Methods:
            Clear Board
            Draw Board
            Get Position on Board
    """

    def __init__(self, rows, columns, blank_symbol):
        self.rows = rows
        self.columns = columns
        self.blank_symbol = blank_symbol
        self.create_positions()


    def create_positions(self):
        self.positions = {}
        for row in range(1, self.rows + 1):
            for column in range(1, self.columns + 1):
                position_key = "{}{}".format(row, column)
                self.positions[position_key] = Position(row=row, column=column, value=blank_symbol)


    def draw_board(self, output_type="v"):
        """
            Print board position symbols in rows/columns
            Use sorted dictionary

            Parameters:
                output_type = (v) or (k)
        """
        output_list = []  #TODO Need row/column headers and spaces between positions
        row_save = 1
        for key, position in sorted(self.positions.items()):
            if position.row != row_save:
                output_list.append("\n")
            if output_type.lower()[0] == "k":
                output_list.append(key)
            else:
                output_list.append(position.value)
            row_save = position.row

        output_str = "".join(output_list)
        print(output_str)


    def get_position(self, row, column):
        """
            Return position object on board
                based on row, column
        """
        position_key = "{}{}".format(row, column)
        return self.positions[position_key]


class Player(object):
    """
        Player playing game

        Properties:
            Name
            Value - used on board position
            Wins - total wins in game
    """

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.wins = 0

    def add_win(self):
        self.wins += 1


class Game(object):
    """
        Game play

        Properties:
            Board Rows
            Board Columns
            Players List

        Methods:
            Play Game
    """

    def __init__(self, board, players):
        self.board = board
        self.game_players = players

    def play_game(self):

        # Setup Game
            # Create Players
            # Create Board
                # Rows?
                # Columns?

        # Play Game
            # Player's Turn
            # Player's Move
                # Row?
                # Column?
                # Must be on board, cannot already have a value
            # Win Condition

        # Welcome message
        print("Welcome to the game")
        print("Here's the empty board")
        self.board.draw_board()

        # Loop through players
        for player in players:
            print("Hey {}, it's your turn".format(player.name))
            # User Input Row        #TODO Check integer digits "x.isdigit()"
            row = int(input("Please enter the row you want to select --> "))
            while row < 1 or row > self.board.rows:
                row = int(input("That row number isn't on the board.  Please enter the row you want to select --> "))
            # User Input Column
            column = int(input("Please enter the column you want to select --> "))
            while column < 1 or column > self.board.columns:
                column = int(input("That column number isn't on the board.  Please enter the column you want to select --> "))

            # Get position on board
            position = self.board.get_position(row, column)
            # Set position on board using player value
            position.value = player.value

            # Print Board
            print("Here's the new board")
            self.board.draw_board()


if __name__ == "__main__":
    new_board = Board(rows=3,columns=3,blank_symbol=".")
    player1 = Player(name="John", value="X")
    player2 = Player(name="Sally", value="Y")
    players = [player1, player2]

    new_game = Game(board=new_board, players=players)
    new_game.play_game()

