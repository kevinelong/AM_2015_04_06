# find where to split where
#  sum of first slice and last slice
# are least different

A = [3, 1, 2, 4, 3]


def best_split(A):
    best = sum(A)
    for i in range(0, len(A) + 1):
        a = sum(A[:i])
        b = sum(A[i:])

        d = abs(b - a)
        print(i, a, b, d)
        if i == 0:
            best = d
        elif d < best:
            best = d
        else:
            return best


print(best_split(A))
