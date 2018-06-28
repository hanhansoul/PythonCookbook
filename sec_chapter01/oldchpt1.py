
"""
makedict可以使得字典的创建更加直观简单，减少引号的使用。
When you declare a function in Python, you may optionally conclude the list of formal arguments
with *args or **kwds (if you want to use both, the one with ** must be last). If you have
*args, your function can be called with any number of extra actual arguments of the positional,
or plain, kind. Python collects all the extra positional arguments into a tuple and binds that tuple to
the identifier args. Similarly, if you have **kwds, your function can be called with any
number of extra actual arguments of the named, or keyword, kind. Python collects all the extra
named arguments into a dictionary (with the names as the keys and the values as the values) and
binds that dictionary to the identifier kwds. This recipe exploits the way that Python knows how
to perform the latter task.
"""
def makedict(**kwargs):
    return kwargs
d = makedict(a = 1, b = 2, c = 3)

"""
1.4 Getting a Value from a Dictionary
If you try to get a value with a syntax such as d[x], and the value of x is not a key in dictionary
d, your attempt raises a KeyError exception.
You get d[x] if x is a key in d, and if it's not, you get None (which you can check for
or propagate). If None is not what you want to get when x is not a key of d, call d.get(x,
somethingelse) instead. In this case, if x is not a key, you will get the value of
somethingelse.
"""
d.get('d')
print(d.get('d'))
print(d.get('d', 'nothing'))


"""
1.5 Adding an Entry to a Dictionary
setdefault()
use the entry if it is already present; otherwise, add a new entry.
"""

print(d.setdefault('a', 100))
print(d.setdefault('d', 100))
print(d)


"""
1.6 Associating Multiple Values with Each Key in a Dictionary
两种方法，取决于如何处理字典中的重复项
允许重复项时，字典中采用各键对应值采用列表存储
不允许重复项时，字典中采用各键对应值<value, bool>类型的字典来存储
"""

key = 'a'
value = 20
d1 = {'a':[1, 2, 3]}
d1.setdefault(key, []).append(value)
print(d1)
d2 = {}
d2.setdefault(key, {})[value] = 1
print(d2)
value = 20

"""
1.8 Collecting a Bunch of Named Items
Any (classic) class inherently wraps a dictionary
when all names are identifiers, to be used just like variables, the dictionary-access syntax is not maximally clear
"""

class BunchD(dict):
    def __init__(self, **kwds):
        dict.__init__(self, kwds)
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

d = BunchD(a = 123, b = 321, c = 199)
print(d.a)
print(d.b)
print(d.c)

"""
1.9 Finding the Intersection of Two Dictionaries
"""
#错误的方法
# O(sizeof(some_dict) * sizeof(another_dict))
some_dict = { 'zope':'zzz', 'python':'rocks' }
another_dict = { 'python':'rocks', 'perl':'$' }
intersect = []
for item in some_dict.keys():
    if item in another_dict.keys():
        intersect.append(item)
print("Intersects:", intersect)

#正确的方法
# O(size of (some_dict))
print("Intersects:", [k for k in some_dict if k in another_dict])

#更快的方法
print(some_dict.has_key('zope'))
#print(filter(some_dict.has_key, another_dict.keys()))


if __name__ == "__main__":
    print('chpt1')





