# Simple Script

a = 2
b = 3
print(a + b)

x = 6
y = 7
print(x + y)


# Eliminate redundancy copy paste code with function
def add_pair(x, y):
    total = x
    total += y
    return total


print(add_pair(2, 3))
print(add_pair(6, 7))

# Eliminate more redundancy by using a collection/list
def add_pairs(pair_list):
    output = list()
    for pair in pair_list:
        output.append(add_pair(pair[0], pair[1]))
    return output


print(add_pairs([[2, 3], [6, 7]]))


class PairList(list):
    def __init__(self, pairs):
        self.extend(pairs)


class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MultiMath(object):
    def __init__(self, pair_list):
        self.pair_list = pair_list

    @staticmethod
    def add_pair(pair):
        total = pair.x
        total += pair.y
        return total

    def add_pairs(self):
        output = []
        for pair in self.pair_list:
            output.append(self.add_pair(pair))
        return output

    def print_pair_sums(self):
        sums = self.add_pairs()
        for s in sums:
            print(s)

print( MultiMath.add_pair(Pair(9,9)))
mm = MultiMath([Pair(2, 3), Pair(6, 7)])
mm.print_pair_sums()
