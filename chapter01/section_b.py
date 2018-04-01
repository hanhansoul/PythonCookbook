def section_1_11():
    """
    1.11 Naming a Slice
    从特定格式的数据中利用slice提取需要的内容，通过对slice进行命名，避免随处出现的切片索引硬编码的情况。
    """

    def test1():
        record = "aaaaaaaaaa100aaaaaaaaaa513.25aaaaaaaaaa"
        shares = slice(10, 13)
        price = slice(23, 29)
        # print(record[shares])
        # print(record[price])
        print(int(record[shares]) * float(record[price]))

    def test2():
        """
        slice.indices(len(string))可以消除下标越界的问题。
        """
        a = slice(10, 50, 2)
        s = "HelloWorld"
        a.indices(len(s))
        for i in range(*a.indices(len(s))):
            print(s[i])


def section_1_12():
    """
    1.12. Determining the Most Frequently Occurring Items in a Sequence
    确定一个序列中出现次数最多的项目。

    collections.Counter类中的most_common()函数用于统计序列中出现次数最多的项。
    Counter是一个字典，key为序列中的项，value为该key在序列中出现的次数。
    Counter.update()
    Counter实例可以通过+和-进行运算操作。
    """
    from collections import Counter

    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

    def test1():
        word_counts = Counter(words)
        top_three = word_counts.most_common(3)
        print(top_three)

    def test2():
        a = Counter(words)
        b = Counter(morewords)
        print(a)
        print(b)
        c = a + b
        print(c)
        d = a - b
        print(d)


def section_1_13():
    """
    1.13. Sorting a List of Dictionaries by a Common Key
    通过多个字典中的关键字对一个包含若干字典元素的list排序。

    itemgetter()函数
    """
    from operator import itemgetter

    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

    def test1():
        rows_by_fname = sorted(rows, key=itemgetter('fname'))
        rows_by_uid = sorted(rows, key=itemgetter('uid'))
        print(rows_by_fname)
        print(rows_by_uid)

        rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
        print(rows_by_lfname)

    def test2():
        print(min(rows, key=itemgetter('uid')))
        print(max(rows, key=itemgetter('uid')))


def section_1_14():
    """
    1.14. Sorting Objects Without Native Comparison Support
    对本身不支持比较操作的对象进行排序

    sorted()函数中的参数key可以指定对象中用于排序的属性
    attrgetter()函数
    """

    from operator import attrgetter

    class User:
        def __init__(self, user_id):
            self.user_id = user_id

        def __repr__(self):
            return 'User({})'.format(self.user_id)

    def test1():
        users = [User(23), User(3), User(99)]
        print(sorted(users, key=lambda u: u.user_id))
        print(sorted(users, key=attrgetter('user_id')))


def section_1_15():
    """
    1.15. Grouping Records Together Based on a Field
    根据序列元素中的某一个属性分组并进行遍历

    itertools.groupby()函数
    """
    from operator import itemgetter
    from itertools import groupby

    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    def test1():
        rows.sort(key=itemgetter('date'))

        for date, items in groupby(rows, key=itemgetter('date')):
            print(date)
            for i in items:
                print('     ', i)


def section_1_16():
    """
    1.16. Filtering Sequence Elements
    根据条件对list中的元素进行筛选。

    一般可以采用list compression，但缺点是一次性可能产生大量数据，导致内存溢出。此时可以将list compression转换为
    迭代器方式。
    itertools.compress(elements, condition)函数将boolean类型condition列表中各元素的值，对elements列表元素依
    次进行筛选，只保留condition中为True的元素对应的elements中的元素。
    """

    def test1():
        mylist = [1, 4, -5, 10, -7, 2, 3, -1]
        print([n for n in mylist if n > 0])
        print([n for n in mylist if n < 0])
        # [n for n in mylist if n > 0]的方式在列表包含大量元素时可能消耗大量空间
        # 此时可以利用generator来解决这个问题
        pos = (n for n in mylist if n > 0)
        for x in pos:
            print(x)

    def test2():
        # 将一个函数作为筛选的条件
        values = ['1', '2', '-3', '-', '4', 'N/A', '5']

        def is_int(val):
            try:
                x = int(val)
                return True
            except ValueError:
                return False

        ivals = list(filter(is_int, values))
        print(ivals)

    def test3():
        mylist = [1, 4, -5, 10, -7, 2, 3, -1]
        clip_neg = [n if n > 0 else 0 for n in mylist]
        print(clip_neg)

    def test4():
        from itertools import compress

        addresses = [
            '5412 N CLARK',
            '5148 N CLARK',
            '5800 E 58TH',
            '2122 N CLARK'
            '5645 N RAVENSWOOD',
            '1060 W ADDISON',
            '4801 N BROADWAY',
            '1039 W GRANVILLE',
        ]
        counts = [0, 3, 10, 4, 1, 7, 6, 1]
        more5 = [n > 5 for n in counts]
        print(list(compress(addresses, more5)))


def section_1_17():
    """
    1.17. Extracting a Subset of a Dictionary
    获取dict的子集

    dict comprehension
    """

    def test1():
        prices = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }
        p1 = {key: value for key, value in prices.items() if value > 200}
        print(p1)

        tech_names = {'APPL', 'IBM', 'HPQ', 'MSFT'}
        p2 = {key: value for key, value in prices.items() if key in tech_names}
        print(p2)


def section_1_18():
    """
    1.18. Mapping Names to Sequence Elements
    通过别名而不是元素索引来访问list或tuple中的元素

    collections.namedtuple
    便于修改实例属性的数据结构，namedtuple的替代品__slots__。
    """

    def test1():
        from collections import namedtuple

        Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
        sub = Subscriber('jonesy@example.com', joined='2012-10-19')
        print(sub)
        print(sub.addr)
        print(sub.joined)


def section_1_19():
    """
    1.19. Transforming and Reducing Data at the Same Time

    """

    def test1():
        nums = [1, 2, 3, 4, 5]
        # 效率较低，不够优雅
        # s = sum([x * x for x in nums])
        s = sum(x * x for x in nums)
        print(s)


def section_1_20():
    """
    1.20. Combining Multiple Mappings into a Single Mapping

    对多个dict执行并集操作，合成一个dict。
    ChainMap()函数中参数的顺序决定了出现重复键时候的对应值总是靠前的dict中的值。
    """

    def test1():
        from collections import ChainMap

        a = {'x': 1, 'z': 3}
        b = {'y': 2, 'z': 4}
        c = ChainMap(a, b)
        print(c)

    def test2():
        s1 = {1, 3, 5, 7}
        s2 = {2, 4, 6, 8}
        print(s1 - s2)
