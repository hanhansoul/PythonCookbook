import itertools
from collections import deque


def output(ii):
    for i in ii:
        print(i)


#
# c = itertools.count(10)
#
# output(itertools.islice('ABCDEFG', 2))
#
# s0 = itertools.islice(iter([40, 30, 50, 46, 39, 44]), 2)
# s1 = itertools.islice([40, 30, 50, 46, 39, 44], 2)


def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n - 1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n


output(moving_average([40, 30, 50, 46, 39, 44]))
