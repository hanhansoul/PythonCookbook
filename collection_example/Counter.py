from collections import Counter

"""
Counter提供了一个方便高效的计数器对象

Counter是dict的子类，以哈希表方式保存各个对象的数量，支持所有dict方法。
Counter等同于C++中的multiset，可保存重复键的set。

elements()
根据Counter中各元素及元素对应数量，返回一个包含相应数量元素的迭代器，返回元素顺序是随机的。

most_common([n])
按照元素频数从高到底的顺序返回出现频数最高的前n个元素与其数量的列表，各元素与其数量以tuple保存。
c.most_common()[:-n-1:-1] # 返回频数最少的前n个元素

subtract()
将两个Counter对象中的元素的数量相减。

"""

cnt = Counter()

for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

c = Counter()  # empty Counter
c = Counter('gallahad')  # iterable
c = Counter({'red': 4, 'blue': 2})  # mapping
c = Counter(cats=4, dogs=6)  # keyword args

c = Counter(a=4, b=2, c=0, d=-2)
sorted(c.elements())

sum(c.values())
c.items()
list(c)
set(c)
dict(c)
+c  # 删除数量为0或负数的元素
-c  # 删除数量为0或负数的元素，并将所有负数变为其相反数

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print(c + d)    # c[x] + d[x]
print(c - d)    # c[x] - d[x]
print(c & d)    # 交集 min(c[x], d[x])
print(c | d)    # 并集 max(c[x], d[x])
