from collections import defaultdict

"""
defaultdict是dict的子类，支持所有dict方法。

defaultdict([default_factory[,...]])
default_factory为defaultdict中键值对的值提供一个工厂方法，可以根据提供的default_factory指定字典中
值的类型，并以此确定针对值类型方法。

defaultdict可以用于实现multidict。

__missing__(key)

default_factory

"""

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
sorted(d.items())

# 等同于setdefault()
dx = {}
for k, v in s:
    d.setdefault(k, []).append(v)

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
sorted(d.items())

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)
sorted(d.items())
