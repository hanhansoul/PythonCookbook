"""
1.1. Unpacking a Sequence into Separate Variables
Any sequence (or iterable) can be unpacked into variables using a simple assignment operation.
Unpacking actually works with any object that happens to be iterable, not just tuples or lists.
This includes strings, files, iterators, and generators.
"""
a, b, c = (1, 2, 3)
#print(a, b, c)
#When unpacking, you may sometimes want to discard certain values. Pick a throwaway variable name for it
_, shares, price, _ = [ 'ACME', 50, 91.1, (2012, 12, 21) ]


"""
1.2. Unpacking Elements from Iterables of Arbitrary Length
You need to unpack N elements from an iterable, but the iterable may be longer than N elements,
causing a “too many values to unpack” exception.
Python “star expressions” can be used to address this problem.
一个赋值表达式终不能出现两个*变量
"""
user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
#print(name, email, phone_numbers)
*trailing, current0, current1 = [10, 8, 7, 1, 9, 5, 10, 3]
#print(trailing, current0, current1)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

"""
1.3. Keeping the Last N Items
    Keeping a limited history is a perfect use for a collections.deque .
Using deque(maxlen=N) creates a fixed-sized queue. When new items are added and
the queue is full, the oldest item is automatically removed.

    More generally, a deque can be used whenever you need a simple queue structure.
deque.append() / deque.appendleft() / deque.pop() / deque.popleft()
"""
from collections import deque
q = deque(maxlen = 3)
q.append(1)
q.append(2)
q.append(3)
#print(q)
q.append(4)
#print(q)
#
q = deque()
q.append(1)
q.append(2)
q.append(3)
#print(q)
q.appendleft(4)
#print(q)
q.pop()
q.popleft()
#print(q)

"""
1.4. Finding the Largest or Smallest N Items
    The heapq module has two functions—nlargest() and nsmallest()—that do exactly what you want.
heapq是一个最小堆
heapq.heappop() / heapq.heappush()
heapq.min() / heapq.max()
"""

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
#print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
#print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
#print(cheap)
#print(expensive)

heap = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.heapify(heap)
#print(heap)
#print(heapq.heappop(heap))
#print(heapq.heappop(heap))

"""
1.5. Implementing a Priority Queue
利用tuple (priority, index, item) 实现堆中对各项的权值比较
#python中没有现成的priority_queue !?
"""
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

"""
1.6. Mapping Keys to Multiple Values in a Dictionary
    Multidicts store the multiple values in another container such as a list or set.
Use a list if you want to preserve the insertion order of the items. Use a set if you want to eliminate
duplicates (and don’t care about the order).
    To easily construct such dictionaries, you can use defaultdict in the collections
module. A feature of defaultdict is that it automatically initializes the first value so
you can simply focus on adding items.
    One caution with defaultdict is that it will automatically create dictionary entries for
keys accessed later on (even if they aren’t currently found in the dictionary). If you don’t
want this behavior, you might use setdefault() on an ordinary dictionary instead.

# defaultdict(function_factory)构建的是一个类似dictionary的对象，其中keys的值，自行确定赋值，但是values的类型，
是function_factory的类实例，而且具有默认值。比如default(int)则创建一个类似dictionary对象，里面任何的values都是int的实例，
而且就算是一个不存在的key, d[key] 也有一个默认值，这个默认值是int()的默认值0.
# 使用list时，允许同一个key对应多个重复的value
# 使用set时，每一个key只能对应多个不重复的value
"""
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(1)
d['b'].append(3)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(1)
d['a'].add(2)
d['b'].add(2)
#print(d)


"""
1.7. Keeping Dictionaries in Order
    Control the order of items in a dictionary when iterating or serializing.
# OrderedDict exactly preserves the original insertion order of data when iterating.
"""
from collections import OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
del d['c']
#print(d)

"""
1.8. Calculating with Dictionaries
    Perform various calculations (e.g., minimum value, maximum value, sorting, etc.) on a dictionary of data.
#   zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），
    然后返回由这些tuples组成的list（列表）。若传入参数的长度不等，则返回list的长度和参数中长度最短的对象相同。
    利用*号操作符，可以将list unzip（解压）
#   zip()实现了行列式的行列互换操作
    zip() creates an iterator that can only be consumed once.
"""
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))

"""
1.9. Finding Commonalities in Two Dictionaries
#   求字典的交集与差集。注：values()不满足这类操作，因为其具有不唯一性，可以先用defaultdict(set)进行替换。
dict.items() / dict.keys() / dict.values()
"""
a = {'x' : 1, 'y' : 2, 'z' : 3}
b = {'w' : 10, 'x' : 11, 'y' : 2}
# Find keys in common
print(a.keys() & b.keys())
# Find keys in a that are not in b
print(a.keys() - b.keys())
# Find (key,value) pairs in common
print(a.items() & b.items())

"""
???
1.10. Removing Duplicates from a Sequence while Maintaining Order
Eliminate the duplicate values in a sequence, but preserve the order of the
remaining items.
"""




















