from collections import OrderedDict

"""
OrderedDict对象与dict类似，但是其保存了item插入字典的顺序。
当遍历OrderedDict时，item将按照其插入字典的顺序返回。
OrderedDict是dict的子类，支持dict方法。

OrderedDict([items])

popitem(last=Ture)
删除并返回最后/第一个键值对。

move_to_end(key, last=True)
将一个已有的键移动到OrderedDict的首位/末位。

reversed()

两个OrderedDict间的比较要求键值对的顺序也要相同。

"""

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
OrderedDict(sorted(d.items(), key=lambda t: t[0]))
OrderedDict(sorted(d.items(), key=lambda t: t[1]))
OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))


class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)


class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)
