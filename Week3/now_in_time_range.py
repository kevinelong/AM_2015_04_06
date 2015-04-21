from datetime import datetime


def in_range(test, start, stop):
    if test > start:
        if test < stop:
            return True
    return False


if __name__ is "__main__":
    test = datetime.now().time()
    start = datetime(1970, 1, 1, 9, 0).time()
    stop = datetime(1970, 1, 1, 16, 0).time()
    print(test, start, stop)
    print(in_range(test, start, stop))