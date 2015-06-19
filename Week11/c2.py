# how many steps at rate per step to reach goal
# from current position
import math


def get_steps(X, Y, D):
    dist = Y - X
    return math.ceil(dist / D)

    # count = 0
    # prog = 0
    # while prog < dist:
    #
    #     prog += D
    #     count+=1

    # return count


print(get_steps(10, 85, 30))
