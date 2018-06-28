import itertools

"""
4.1. Manually Consuming an Iterator
#   You need to process items in an iterable, but for whatever reason, you can’t or don’t want
#   to use a for loop.
    使用next(it)遍历迭代器时，需要注意其结束条件。在结束时，next()会抛出StopIteration异常。
"""


"""
4.2. Delegating Iteration
#   make iteration work with your new customized container.
    覆盖__iter__()方法
"""
'''
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
#for ch in root:
#    print(ch)
'''

"""
### 生成器和yield
#   在使用迭代器遍历list，tuple，string时，你可以重复读取其中的值，但要求所迭代的对象全部预先存储在内存中。
#   生成器同样是可迭代对象，但是你只能读取一次，因为它并没有把所有值存放内存中，而是动态的生成读取的值。

#   yield是关键字，用起来像return。yield要求函数返回一个生成器。
"""
'''
# for i in mylist 使用了迭代器。
mylist = [x * x for x in range(3)]
for i in mylist :
    pass

# mygenerator为一个生成器
mygenerator = (x * x for x in range(3))
for i in mygenerator :
    pass
'''

# yield
"""
#   当你调用生成器函数的时候，如createGenerator()，程序并不会执行函数体内的代码，它仅仅只是返回
#   生成器对象，这种方式颇为微妙。函数体内的代码只有直到每次循环迭代(for)生成器的时候才会运行。
"""
'''
def createGenerator():
    print('start createGenerator')
    mylist = range(3)
    for i in mylist :
        yield i * i

# create a generator
mygenerator = createGenerator()
# mygenerator is an object!
# print(mygenerator)
# 开始迭代时才执行函数createGenerator，打印start createGenerator。
for i in mygenerator:
    pass
class Bank():
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$100"

"""
"""
def gen():
    for x in range(4):
        tmp = yield x
        if tmp == 'hello':
            print('world')
        else:
            print(str(tmp))

g = gen()
#print(g.__next__())
#print(g.__next__())
#print(g.send('hello'))
'''

"""
4.3. Creating New Iteration Patterns with Generators
#   You want to implement a custom iteration pattern that’s different than the
#   usual builtin functions (e.g., range(), reversed(), etc.).

#   If you want to implement a new kind of iteration pattern, define it using a generator
#   function.
"""
'''
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

#for n in frange(0, 4, 0.5):
#    print(n)
#print(list(frange(0, 1, 0.125)))
'''

"""
4.4. Implementing the Iterator Protocol
#   yield from ???
"""
'''
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self, node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))
#for ch in root.depth_first():
#    print(ch)
'''

"""
4.5. Iterating in Reverse
#   iterate in reverse over a sequence.
#   reversed() / __reversed__()
#   reversed() 只接受可迭代对象，如list, tuple
"""
'''
li = [1, 2, 3, 4, 5]
#for x in reversed(li):
#   print(x)

class Countdown:
    def __init__(self, start):
        self.start = start
    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

#tu = (1, 2, 3, 4)
#for x in reversed(tu):
#    print(x)
'''

"""
4.6. Defining Generator Functions with Extra State
"""

"""
4.7. Taking a Slice of an Iterator
#   itertools.islice()
"""
'''
def count(n):
    while n < 100:
        yield n
        n += 1

print(list(count(0)))
for x in itertools.islice(count(0), 10, 20):
    print(x)
'''

"""
4.8. Skipping the First Part of an Iterable
#   itertools.dropwhile()
"""

#with open('input_4_8') as fin:
#    for line in itertools.dropwhile(lambda line: line.startswith('#'), fin):
#        print(line, end = '')

items = ['a', 'b', 'c', 1, 4, 10, 15]
#for x in itertools.islice(items, 3, None):
#    print(x)

"""
4.9. Iterating Over All Possible Combinations or Permutations
#   itertools.permutations()
#   itertools.combinations()
"""
'''
li = [1, 2, 3]
for p in itertools.permutations(li):
    print(p)

for p in itertools.permutations(li, 2):
    print(p)

for c in itertools.combinations(li, 3):
    print(c)

for c in itertools.combinations_with_replacement(li, 3):
    print(c)
'''

"""
4.10. Iterating Over the Index-Value Pairs of a Sequence
#   You want to iterate over a sequence, but would like to keep track of which element of
#   the sequence is currently being processed.
#   enumerate()
"""
'''
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 2):
    print(idx, val)
'''

"""
4.11. Iterating Over Multiple Sequences Simultaneously
#   zip()
#   itertools.zip_longest()
"""
'''
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x,y)

print(list(zip(xpts, ypts)))
'''

"""
4.12. Iterating on Items in Separate Containers
#   itertools.chain()
"""
'''
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
c = ['ab', 'bc', 'cd']
for x in itertools.chain(a, b, c):
    print(x)
'''

"""
4.13. Creating Data Processing Pipelines
#   you have a huge amount of data that needs to be processed, but it can’t fit
#   entirely into memory.
"""
'''
import os
import fnmatch
import gzip
import bz2
import re
'''

"""
4.14. Flattening a Nested Sequence
"""
'''
def foo():
    lst = []
    for i in range(4):
        lst.append(lambda: i)
    print([f() for f in lst])

foo()
'''
'''
i = 1

def foo():
    i = 4
    i += 1
    print(i, 'in foo()')

foo()
print(i, 'global')
'''
'''
a_var = 'global value'

def outer():
    a_var = 'enclosed value'
    print(a_var)
    def inner():
        nonlocal a_var
        a_var = 'local value'
        print(a_var)

    print(a_var)
    inner()
    print(a_var)

outer()
print(a_var)

'''

"""
1.  python多重继承的继承顺序 MRO 3C
2.  python3 super().__init() / baseClassName.__init__(self)
3.  python的作用域 LEGB原则
    def / lambda 定义新的作用域scopes，class只有命名空间namespace，不产生新的作用域
    if / for / while 为块blocks，不产生新的作用域
4.  global varName / nonlocal varName
"""
