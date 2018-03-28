def outer(func):
    def inner():
        print("before func")
        ret = func()
        return ret + 1

    return inner


@outer
def foo():
    return 1


foo()


def spam():
    return 1


outer(spam)()


# if __name__ == "__main__":

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord: " + str(self.__dict__)


