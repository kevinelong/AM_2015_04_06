__author__ = 'kevinlong'

d = {"A": 123}
print(d["A"])

x = 456
d["A"] = x

print(d["A"])

x = 789

print(d["A"])

e = {"B": 123}
print(e["B"])

y = [456]
e["B"] = y

print(e["B"])

# y = [789]
y[0] = 789


print(e["B"])



f = {"C": 123}
print(f["C"])

y = {"V":456}
f["C"] = y

print(f["C"])

# y = [789]
y["V"] = 789


print(f["C"])
