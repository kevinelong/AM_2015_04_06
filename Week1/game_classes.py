# tic tac toe

# What are the things/nouns in the game? board, x's, o's, blanks, lines
# What are the actions/verbs? whose turn it is, piece being added, next person's turn
# What properties and parameters for each? location, type added, result(win or whatnot)

# How can we support any board size?
# How can we support any number of players and symbols?

# EXAMPLE USE
# players = []
# players.append(Player('Player One', 'X'))
# players.append(Player('Player Two', 'O'))
# players.append(Player('Player Three', 'Z'))
#
# board_size = 9
# goal_in_a_row = 5
# games_instance = Game(players, board_size, goal_in_a_row)
# games_instance.play_game()

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