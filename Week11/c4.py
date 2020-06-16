# find the longest cumulative length of two contiguous ranges,
# where the first has mostly zeros
# and the second has mostly ones.
# Estimated time to complete 90 minutes.
A = [1, 1, 0, 1, 0, 0, 1, 1]
# answer would be 7 as 2nd through 6th plus 7th through 8th are the sets.

def get_length(A):
    best = 0
    list_length = len(A)

    for start in range(0, list_length + 1):
        for end in range(start + 1, list_length + 1):
            first = sum(A[start:end])
            if first < ((end - start) / 2.0):
                for start2 in range(end + 1, list_length + 1):
                    for end2 in range(start2 + 1, list_length + 1):
                        second = sum(A[start2:end2])
                        if second > ((end2 - start2) / 2.0):
                            length = end2 - start
                            if length > best:
                                best = length
                                # print(start, end, start2, end2)
    return best


print(get_length(A))
