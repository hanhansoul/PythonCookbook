def chapter_4_12():
    def test1():
        from itertools import chain
        a = [1, 2, 3, 4]
        b = ['x', 'y', 'z']
        for x in chain(a, b):
            print(x)


def chapter_4_13():
    pass


def chapter_4_14():
    from collections import Iterable

    def test1():
        def flatten(items, ignore_types=(str, bytes)):
            for x in items:
                if isinstance(x, Iterable) and not isinstance(x, ignore_types):
                    yield from flatten(x)
                    # for i in flatten(x):
                    #     yield i
                else:
                    yield x

        items = [1, 2, [3, 4, [5, 6], 7], 8]
        for x in flatten(items):
            print(x)


def chapter_4_15():
    pass


def chapter_4_16():
    pass
