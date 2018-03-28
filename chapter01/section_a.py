def section_1_1():
    """
    1.1 Unpacking a Sequence into Separate Variables
    将tuple或sequence拆分成若干独立的变量

    通过简单的赋值操作就可以实现，任意可迭代对象都支持该操作，不限于tuple/list等。

    a, b, c ==> (a, b, c)
    """

    def test1():
        p = (4, 5)
        x, y = p
        print(x, y)

    def test2():
        s = "Hello"
        a, b, c, d, e = s
        print(a, b, c, d, e)

    def test3():
        data = ['ACME', 50, 91.1, (2012, 12, 21)]
        name, shares, price, (year, mon, day) = data


def section_1_2():
    """
    1.2. Unpacking Elements from Iterables of Arbitrary Length
    需要从一个可迭代容器中拆分出N个元素，但该容器可能包含超过N个元素。

    python使用*符号来匹配变长的序列，其返回的变量始终是一个list
    """

    def test1():
        record = ("Dave", "dave@example.com", "773-555-1212", "847-555-1212")
        name, email, *phone_numbers = record
        print(phone_numbers)

    def test2():
        records = [('foo', 1, 2),
                   ('bar', 'hello'),
                   ('foo', 3, 4), ]

        def do_foo(x, y):
            print("foo", x, y)

        def do_bar(s):
            print("bar", s)

        for tag, *args in records:
            if tag == "foo":
                do_foo(*args)
            elif tag == "bar":
                do_bar(*args)

    def test3():
        line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
        uname, *fields, homedir, sh = line.split(":")
        print(fields)
        print(uname, homedir, sh)

    def test4():
        record = ('ACME', 50, 123.45, (12, 18, 2012))
        name, *_, (*_, year) = record
        print(name, year)


def section_1_3():
    """
    1.3. Keeping the Last N Items
    保留某次迭代过程的最近几条记录

    使用双端队列deque。当队列装满后，队尾新添加的元素将把最早添加的元素从队首删除。

    在指定了deque的maxlen属性后，deque中最多保留maxlen个元素，多余元素将按照插入的顺序
    被删除。
    """

    def test1():
        """
        When writing code to search for items, it is common to use a generator function involving
        yield, as shown in this recipe’s solution. This decouples the process of searching
        from the code that uses the results.
        """
        from collections import deque

        def search(lines, pattern, history=5):
            previous_lines = deque(maxlen=history)
            for line in lines:
                if pattern in line:
                    yield line, previous_lines
                previous_lines.append(line)

        with open("chapter01/file.txt") as f:
            for line, prevlines in search(f, "python", 5):
                for pline in prevlines:
                    print(pline, end="")
                print(line, end="")
                print('-' * 20)


def section_1_4():
    """
    1.4. Finding the Largest or Smallest N Items
    返回容器中最大和最小的若干项的list

    使用heapq的nlargest()/nsmallest()函数。
    """
    import heapq

    def test1():
        nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
        print(heapq.nlargest(3, nums))
        print(heapq.nsmallest(3, nums))

    def test2():
        portfilio = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
                     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                     {'name': 'FB', 'shares': 200, 'price': 21.09},
                     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                     {'name': 'ACME', 'shares': 75, 'price': 115.65}
                     ]
        cheap = heapq.nsmallest(3, portfilio, key=lambda s: s["price"])
        expensive = heapq.nlargest(3, portfilio, key=lambda s: s["price"])
        print(cheap, expensive)

    def test3():
        nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
        heap = list(nums)
        heapq.heapify(heap)
        print(heap)


def section_1_5():
    """
    1.5. Implementing a Priority Queue
    堆。
    heapq.heappush() / heapq.heappop()
    """
    import heapq

    class PriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0

        def push(self, item, priority):
            heapq.heappush(self._queue, (-priority, self._index, item))
            self._index += 1

        def pop(self):
            return heapq.heappop(self._queue)[-1]


def section_1_6():
    """
    1.6. Mapping Keys to Multiple Values in a Dictionary
    实现multidict。

    使用list或set类型作为dict的键对应的值。使用defaultdict能够自动初始化第一个值，我们只需要关注
    添加新的值就行了。
    """
    from collections import defaultdict

    def test1():
        d = defaultdict(list)
        d['a'].append(1)
        d['a'].append(2)
        d['b'].append(4)
        print(d)

    def test2():
        d = defaultdict(set)
        d['a'].add(1)
        d['a'].add(2)
        d['b'].add(4)
        print(d)


def section_1_7():
    """
    1.7. Keeping Dictionaries in Order
    控制dict中遍历元素的顺序。

    OrderdDict保留了元素插入dict的顺序。
    """

    from collections import OrderedDict

    def test1():
        d = OrderedDict()
        d['foo'] = 1
        d['bar'] = 2
        d['spam'] = 3
        d['grok'] = 4
        print(d)
        for key in d:
            print(key, d[key])


def section_1_8():
    """
    1.8. Calculating with Dictionaries
    计算dict中数据的最大值、最小值，对dict数据进行排序等。

    zip()函数将字典装换成了(value, key)对的一个序列。
    """

    def test1():
        prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }
        prices_and_names = zip(prices.values(), prices.keys())
        # print(prices_and_names)
        print(min(zip(prices.values(), prices.keys())))
        print(max(zip(prices.values(), prices.keys())))
        print(sorted(zip(prices.values(), prices.keys())))


def section_1_9():
    """
    1.9. Finding Commonalities in Two Dictionaries
    返回两个dict中键值对相同的项，即求两个dict的交集。

    python中使用&、|、-即可实现集合的交、并和差运算。
    dict.keys()返回所有的键。
    dict.values()返回所有的值，values()的返回值不支持集合运算，因为其不具有唯一性。
    dict.items()返回所有的键值对。
    """

    def test1():
        a = {
            'x': 1,
            'y': 2,
            'z': 1
        }
        b = {
            'w': 10,
            'x': 11,
            'y': 2
        }
        # print(a.values())
        print(a.keys() & b.keys())
        print(a.keys() - b.keys())
        print(a.items() & b.items())
        print(a.items() | b.items())
        print(set(a.values()) & set(b.values()))

    def test1():
        a = {
            'x': 1,
            'y': 2,
            'z': 1
        }
        c = {key: a[key] for key in a.keys() - {'z', 'w'}}
        print(c)


def section_1_10():
    """
    1.10. Removing Duplicates from a Sequence while Maintaining Order
    删除sequence中的重复项，并保留原sequence的顺序。

    使用set和一个生成器，其中set用于判重，依次输出不重复的项。
    这种方法仅适用于序列中的项是可哈希的。

    对于不可哈希的项目，如dicts，需要稍作修改。
    添加参数key，key将指定一个函数将序列的项转换为可哈希的类型。

    如果仅仅是需要将序列中的重复项去掉，则创建一个set就可以满足要求了。
    > a = [1, 5, 2, 1, 9, 1, 5, 19]
    > set(a)
    {1, 2, 10, 5, 9}
    """

    def test1():
        def dequpe(items):
            seen = set()
            for item in items:
                if item not in seen:
                    yield item
                    seen.add(item)

        a = [1, 5, 2, 1, 9, 1, 5, 10]
        print(list(dequpe(a)))

    def test2():
        def dedupe(items, key=None):
            seen = set()
            for item in items:
                val = item if key is None else key(item)
                if val not in seen:
                    yield item
                    seen.add(val)

        a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
        print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
        print(list(dedupe(a, key=lambda d: d['x'])))
