def chapter_4_11():
    """
    zip()
    itertools.zip_longest()
    并行迭代
    """

    def test1():
        xpts = [1, 5, 4, 2, 10, 7]
        ypts = [101, 78, 37, 15, 62, 99]
        for x, y in zip(xpts, ypts):
            print(x, y)


def chapter_4_12():
    """
    itertools.chain
    """

    def test1():
        from itertools import chain
        a = [1, 2, 3, 4]
        b = ['x', 'y', 'z']
        for x in chain(a, b):
            print(x)


def chapter_4_13():
    """
    管道
    """
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
    """
    合并已排序的序列并输出。
    """
    import heapq

    def test1():
        a = [1, 4, 7, 10]
        b = [2, 5, 6, 11]
        for c in heapq.merge(a, b):
            print(c)


def chapter_4_16():
    pass
