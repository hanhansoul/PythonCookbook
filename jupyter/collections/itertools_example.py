import itertools
import functools
from collections import deque

"""
itertools提供高效的迭代器


"""


def output(ii):
    for i, c in enumerate(ii):
        if i > 20:
            break
        print(c)


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

# count(start[, step]) 无限递增计数器
output(itertools.count(10))
output(zip(itertools.count(10, 2), [1, 2, 3, 4, 5]))

# cycle(p) 无限循环器
itertools.cycle('ABCD')

# repeat(elem[, n]) 重复无限次或n次
itertools.repeat(10, 3)

# 累加器
# itertools.accumulate(iterable, func=operator.add)
output(itertools.accumulate([1, 2, 3, 4, 5]))
print(functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 0))

# itertools.chain() / itertools.chain.from_iterable()
# 连接多个可迭代对象
it1 = iter(list('ABC'))
it2 = iter(list('DEF'))
it3 = iter(list('GHI'))
output(itertools.chain(it1, it2, it3))
output(itertools.chain('ABC', 'DEF', 'GHI'))
output(itertools.chain.from_iterable(['ABC', 'DEF', 'GHI']))

# itertools.compress()
# 过滤器
output(itertools.compress('abcdefg', [1, 0, 1, 0, 0, 1, 1]))

# itertools.dropwhile() / itertools.takewhile()
output(itertools.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
output(itertools.takewhile(lambda x: x < 5, [1, 4, 6, 4, 1]))

# 过滤器
output(itertools.filterfalse(lambda x: x % 2, range(10)))
output(filter(lambda x: x % 2, range(10)))

# 分组
# itertools.groupby()
output(itertools.groupby('AAAABBBCCDAABBB'))

# itertools.islice(seq, [start,] stop, [step])
itertools.islice('ABCDEFG', 2, None)

# itertools.starmap(func, seq)
output(itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)]))
output(map(pow, [2, 3, 10], [5, 2, 3]))

# itertools.tee()
# 为一个可迭代对象返回n个独立的迭代器
output(itertools.tee([1, 2, 3, 4, 5], 2)[1])

# itertools.zip_longest()
output(itertools.zip_longest('ABCD', 'xy', fillvalue='-'))

# itertools.product() 笛卡尔积

# itertools.permutations(p[, r]) 排列

# itertools.combinations(p, r) 组合

# itertools.combinations_with_replacement(p, r) 允许重复的组合
