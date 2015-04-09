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
                self.positions[position_key] = Position(row=row, column=column, value=self.blank_symbol)


    def draw_board(self, output_type="v"):
        """
            Print board position symbols in rows/columns
            Use sorted dictionary


            Parameters:
                output_type = (v)alue or (k)ey
        """
        output_list = []

        # Print column headers
        output_list.append("  ")
        for n in range(1, self.columns + 1):
            output_list.append("{} ".format(n))
        output_list.append("\n")

        # Print row headers and position data
        row_save = 1
        output_list.append("1 ")
        for key, position in sorted(self.positions.items()):
            if position.row != row_save:
                output_list.append("\n")
                # Print row header
                output_list.append("{} ".format(position.row))

            if output_type.lower()[0] == "k":
                output_list.append(key)
            else:
                output_list.append(position.value)
            output_list.append(" ")

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

    output = []

    def __init__(self, board, players):
        self.board = board
        self.game_players = players


    def print_output(self):
        output_str = "".join(self.output)
        print(output_str)
        self.output = []


    def display_board(self):
        self.board.draw_board()


    def welcome_message(self):
        self.output.append("Welcome to the game\nHere's the empty board")
        self.print_output()
        self.display_board()


    def input_row(self):
        input_row = input("Please enter the row you want to select --> ")
        while input_row.isdigit() == False or int(input_row) < 1 or int(input_row) > self.board.rows:
            input_row = input("That row number isn't on the board.  Please enter the row you want to select --> ")
        return input_row


    def input_column(self):
        input_column = input("Please enter the column you want to select --> ")
        while input_column.isdigit() == False or int(input_column) < 1 or int(input_column) > self.board.columns:
            input_column = input("That column number isn't on the board.  Please enter the column you want to select --> ")
        return input_column


    def position_is_empty(self, position):
        if position.value == self.board.blank_symbol:
            return True
        else:
            return False


    def player_turn(self, player):
        print("Hey {}, it's your turn".format(player.name))

        input_row = self.input_row()
        input_column = self.input_column()
        turn_position = self.board.get_position(input_row, input_column)
        while not self.position_is_empty(turn_position):
            print("THAT POSITION IS NOT EMPTY")
            input_row = self.input_row()
            input_column = self.input_column()
            turn_position = self.board.get_position(input_row, input_column)

        #TODO Add win condition
        turn_position.value = player.value

        print("Here's the new board")
        self.display_board()



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


        self.welcome_message()

        end_game = False

        while not end_game:
            for player in players:
                end_game = self.player_turn(player)



if __name__ == "__main__":
    new_board = Board(rows=3,columns=3,blank_symbol=".")
    player1 = Player(name="John", value="X")
    player2 = Player(name="Sally", value="Y")
    players = [player1, player2]

    new_game = Game(board=new_board, players=players)
    new_game.play_game()

