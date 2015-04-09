__author__ = 'Cory'

game_state = ['blank', '.', '.', '.', '.', '.', '.', '.', '.', '.']

win_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

def draw():
    print game_state[1:4]
    print game_state[4:7]
    print game_state[7:10]

draw()

def check_win(sym):
    for x, y, z in win_combos:
        win_sum = 0
        for digit in x, y, z:
            if game_state[digit] == sym:
                win_sum += 1
                if win_sum == 3:
                    print "You win!"
                    draw()
                    quit()
            else:
                pass

class Player(object):
    def __init__(self, name):
        self.name = name
        self.piece = 'X'

    def place_piece(self, number):
        place_range = range(0, 10)
        if number in place_range:
            if game_state[number] == '.':
                game_state[number] = self.piece
            else:
                print "That's an invalid location."
                self.place_piece(int(raw_input("Try another spot: ")))


Player1 = Player(raw_input("Player 1 name: "))
Player2 = Player(raw_input("Player 2 name: "))
Player2.piece = 'O'

turns = 1
while turns <= 9:
    try:
        if ((turns % 2 != 0) or turns == 1):
            Player1.place_piece(int(raw_input((Player1.name + " place piece: "))))
            check_win('X')
            draw()
            turns += 1
        else:
            Player2.place_piece(int(raw_input((Player2.name + " place piece: "))))
            check_win('O')
            draw()
            turns += 1
    except ValueError:
        print "Input a number between 1 and 9: "