__author__ = 'Cory'

x = [1,2,3,1,3,3,5,7,1,1]
indx = 0
x_len = len(x)
dup_dict = {}

while indx < x_len:
    dup_count = 0
    base = x[indx]
    for i in x:
        dup_list = []
        if i == base:
            dup_count += 1
            if dup_count >= 2:
                dup_list.append(base)
                dup_list.append(i)
                temp_dict = {i:dup_list}
                dup_dict.update(temp_dict)
    indx += 1
print dup_dict
