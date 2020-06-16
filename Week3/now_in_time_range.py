from datetime import datetime


def in_range(test, start, stop):
    if test > start and test < stop:
            return True
    return False


if __name__ is "__main__":
    test = datetime.now().time()
    start = datetime(1900, 1, 1, 9, 0).time()
    stop = datetime(1900, 1, 1, 15, 0).time()
    print(test, start, stop)
    print(in_range(test, start, stop))