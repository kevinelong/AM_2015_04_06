# how many steps at rate per step to reach goal
# from current position
import math


def get_steps(start, goal, size):
    dist = goal - start
    return math.ceil(dist / size)

print(get_steps(10, 85, 30))
