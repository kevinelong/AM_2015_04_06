def all_optional(*args):
    print(args)
    print(len(args))
    one = args[0]
    # two = args[1]
    print(one)

all_optional('A')

def myfunc(value=None):
    if value is None:
        value = []
    # modify value here