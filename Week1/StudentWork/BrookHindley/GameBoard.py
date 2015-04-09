__author__ = 'Brook'

class Board:

def __init__(


)







game_state = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]


def draw():
    pass  # TODO PRINT GAME BOARD



# EXAMPLE OUTPUT
# O..
# .X.
# ...

game_state[1][1] = 'X'
game_state[0][0] = 'O'

draw()
#
# class Shape:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.description = "This shape has not been described yet"
#         self.author = "Nobody has claimed to make this shape yet"
#
#     def area(self):
#         return self.x * self.y
#
#     def perimeter(self):
#         return 2 * self.x + 2 * self.y
#
#     def describe(self, text):
#         self.description = text
#
#     def authorName(self, text):
#         self.author = text
#
#     def scaleSize(self, scale):
#         self.x = self.x * scale
#         self.y = self.y * scale