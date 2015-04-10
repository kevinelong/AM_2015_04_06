data = [2, 1, 3, 2, 1, 4, 5, 7, 2, 9]
# You should use the built in function set()
# that converts a list into a set of unique values

def get_duplicates(data):
    output = []
    temp = {}
    for d in data:
        if d not in temp.keys():
            temp[d] = 0
        temp[d] += 1
    for k in temp.keys():
        qty = temp[k]
        if qty > 1:
            output.append(k)
    return output
print(data)
print(get_duplicates(data))
print(set(data))
