"""
1.11. Naming a Slice
    slice(start, stop, step)创建了一个分割器
    slice.indices(len)限定stop的长度
"""
li = range(20)
# res0和res1等价
res0 = li[slice(1, 15)]
res1 = li[1 : 15]
#print(res)
#print(li[SLICE])
sl = slice(1, 10, 2)
#print(sl.start, sl.stop, sl.step)
#
s = "HelloWorld"
sl.indices(len(s))

"""
1.12. Determining the Most Frequently Occurring Items in a Sequence
#   Collections.Counter is a dictionary that maps the items to the number of occurrences.
"""
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
#print(top_three)
#
morewords = ['why','are','you','not','looking','in','my','eyes']
#for word in morewords:
#    word_counts[word] += 1
# or
#word_counts.update(morewords)
#
a = Counter(words)
b = Counter(morewords)
c = a + b
d = a - b

"""
1.13. Sorting a List of Dictionaries by a Common Key
You have a list of dictionaries and you would like to sort the entries according to one or more of the dictionary values.
#   根据一个或多个特定的关键字进行排序
#   使用operator.itemgetter()
"""
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
#print(rows_by_fname)
#print(rows_by_uid)

"""
1.14. Sorting Objects Without Native Comparison Support
You want to sort objects of the same class, but they don’t natively support comparison operations.
"""
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)
users = [User(23), User(3), User(99)]
from operator import attrgetter
sorted(users, key=attrgetter('user_id'))
# 与itemgetter相似，也支持多关键字比较。
# by_name = sorted(users, key=attrgetter('last_name', 'first_name'))

"""
1.15. Grouping Records Together Based on a Field
    通过某个字段将记录分组
"""
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

from operator import itemgetter
from itertools import groupby

rows.sort(key = itemgetter('date'))
#for date, items in groupby(rows, key = itemgetter('date')):
#    print(date)
#    for i in items:
#        print(' ', i)

"""
1.16. Filtering Sequence Elements
"""
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# list comprehension
res = [i for i in mylist if i > 0]
# generator expression
pos = (i for i in mylist if i > 0)
#for x in pos:
#    print(x)
# filter()
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
#print(ivals)
# itertools.compress()
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
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n > 5 for n in counts]
#print(list(compress(addresses, more5)))

"""
1.17. Extracting a Subset of a Dictionary
dictionary comprehension
"""
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
p1 = {key : value for key, value in prices.items() if value < 200}
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key,value in prices.items() if key in tech_names }

"""
1.18. Mapping Names to Sequence Elements
#   collections.namedtuple() is actually a factory method that returns a subclass of the standard Python tuple type.
#   reflection
#   One possible use of a namedtuple is as a replacement for a dictionary, which requires
    more space to store. Thus, if you are building large data structures involving dictionaries,
    use of a namedtuple will be more efficient. However, be aware that unlike a dictionary,
    _replace() method makes an entirely new namedtuple with specified values replaced.
a namedtuple is immutable.
"""
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
#print(sub.addr, sub.joined)

"""
1.19. Transforming and Reducing Data at the Same Time
You need to execute a reduction function (e.g., sum(), min(), max()), but first need to
transform or filter the data.
"""
nums = [1, 2, 3, 4, 5]
s = sum((x * x for x in nums))  # Pass generator-expr as argument
s = sum([x * x for x in nums])  # generate a temporary list as argument
s = sum(x * x for x in nums)    # More elegant syntax

# Certain reduction functions such as min() and max() accept a key argument that might
# be useful in situations where you might be inclined to use a generator.
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])

"""
1.20. Combining Multiple Mappings into a Single Mapping
#   collections.ChainMap takes multiple mappings and makes them logically appear as one. However,
    the mappings are not literally merged together.
#   the duplicate key would always refer to the first dict which contains the key
"""
from collections import ChainMap
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
c = ChainMap(a, b)
#print(c['x'], c['y'], c['z'])
# ChainMap.new_child() add a new mapping
# ChainMap.parents discard last mapping
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
#print(values)
values = values.parents
#print(values)

# different from dict.update()
# if any of the original dictionaries mutate, the changes don’t get reflected
# in the merged dictionary. A ChainMap uses the original dictionaries, so it
# doesn’t have this behavior










