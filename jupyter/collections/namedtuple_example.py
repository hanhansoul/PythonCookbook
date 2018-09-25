from collections import namedtuple

"""
namedtuple(typenmae, field_names, verbose=False, rename=False)
namedtuple用于为tuple中各位置的值命名。

namedtuple._make(iterable)
类方法，用于通过一个可迭代对象创建一个新的namedtuple。

namedtuple._asdict()
以namedtuple中的键值对返回一个OrderedDict对象。

namedtuple._replace(**kwargs)
更新替换原namedtuple中的键值对。

namedtuple._source
返回创建该namedtuple的python源代码，可通过exec()执行。

namedtuple._fields
返回namedtuple中的域名，可用于根据已有namedtuple创建新的namedtuple对象。

可以通过继承一个namedtuple类为其添加新的属性和方法。


"""

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
x, y = p

t = [10, 20]
Point._make(t)

p = Point(x=11, y=22)
p._replace(x=33, y=44)

print(p._fields)
Color = namedtuple('Color', 'red, green, blue')
Pixel = namedtuple('Pixel', Point._fields + Color._fields)


class NewPoint(Point):
    """
    __slots__指定了该类的对象能够动态绑定的可选属性名。
    """
    __slots__ = ()

    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)


for p in NewPoint(3, 4), NewPoint(14, 5 / 7):
    print(p)
