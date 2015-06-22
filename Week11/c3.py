# Find the missing element in a series

def find_missing_element(A):
    t = sum(range(0, len(A) + 2))
    return t - sum(A)

print(find_missing_element([2, 3, 1, 5]))
