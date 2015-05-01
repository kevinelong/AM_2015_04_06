def logger(func):
    def inner(*args, **kwargs):  # 1
        print("Arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs)  # 2

    return inner