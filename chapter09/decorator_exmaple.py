def test1():
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

    class Coordinate(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return "Coord: " + str(self.__dict__)


def test2():
    def decorator(a, b, c):
        def outer(func):
            def wrapper(*args, **kwargs):
                print("decorator", a, b, c)
                return func(*args, **kwargs)

            return wrapper

        return outer

    @decorator('a', 'b', 'c')
    def add(a, b):
        return a + b

    res = add(1, 2)
    print(res)

    def addn(a, b):
        return a + b

    res = decorator('a', 'b', 'c')(addn)(1, 2)
    print(res)


def test3():
    """
    使用functools.partial()方法为装饰器添加参数。
    :return:
    """
    import functools

    def decorator(a, b, c, func=None):
        if func is None:
            return functools.partial(decorator, 1, 2, 3)
        else:
            def wrapper(*args, **kwargs):
                print("decorator", a, b, c)
                return func(*args, **kwargs)

            return wrapper

    @decorator('a', 'b', 'c')
    def add(a, b):
        return a + b

    res = add(1, 2)
    print(res)


test3()
