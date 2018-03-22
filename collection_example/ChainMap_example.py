from collections import ChainMap

import os, argparse

"""
ChainMap用于合并多个字典对象，ChainMap底层使用list保存字典，且保存的是字典的可更新视图，一旦底层的
字典被修改。
ChainMap仅仅维护一个底层映射关系的list，并重写了一般的字典操作用于检索list。
其效率比创建一个新字典或多次调用update()函数更高。

ChainMap中的检索按照其中的字典顺序依次查询，指导找到第一个满足的key。而修改删除操作则只对第一个字典有效。

ChainMap支持所有字典方法。

maps
返回一个包含ChainMap中所有字典的有序list。

new_chile(m=None)
返回一个新ChainMap对象，包含一个新映射m，及所有原ChainMap对象中的映射。
d.new_child = ChainMap(m, *d.maps)
该方法创建一个可以修改但不会影响到原ChainMap的新对象。

parents
返回一个除开原ChainMap对象第一个映射的新ChainMap对象。
d.parents = ChainMap(*d.maps[1:])
"""

d1 = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
d2 = {'a': 0, 'b': 10, 'c': 20, 'd': 30, 'e': 40}

c = ChainMap(d1, d2)
c['a']

c1 = ChainMap()
c1['x'] = 1
c1 = c1.new_child()
c1['x'] = 2
c1 = c1.new_child()
c1['x'] = 3
print(c1)

c1 = c1.parents
c1 = c1.parents
print(c1)

# 通过update()合并的字典不会对原字典的修改有响应
a = dict(x=1, z=3)
b = dict(y=2, z=4)
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])
a['x'] = 13
print(merged['x'])
b['y'] = 100
print(merged['y'])
