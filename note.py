# class Person:
#     def __init__(self, first_name):
#         self.first_name = first_name
#
#     @property
#     def first_name(self):
#         return self._first_name
#
#     @first_name.setter
#     def first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Expected a string")
#         self._first_name = value
#
#     @first_name.deleter
#     def first_name(self):
#         raise AttributeError("Can't delete attribute")


"""
__getattribute__() / __getattr__() / __get__()

首先调用__getattribute__()
"""


# class Count:
#
#     def __init__(self, mymin, mymax):
#         self.mymin = mymin
#         self.mymax = mymax
#         # self.current = None
#
#     def __getattribute__(self, item):
#         if item.startswith('cur'):
#             raise AttributeError
#         return object.__getattribute__(self, item)
#         # or you can use ---return super().__getattribute__(item)
#
#
# obj1 = Count(1, 10)
# print(obj1.mymin)
# print(obj1.mymax)
# print(obj1.current)
#
#
# class D:
#     pass
#
#
# d = D()
# D.__set__(d, )


def test1():
    # Descriptor attribute for an integer type-checked attribute
    """
        Integer是一个data descriptor。因此所有对descriptor值的访问都优先通过__get__()，无论obj.__dict__中是否包含
    该变量。
    """

    class Integer:
        def __init__(self, name):
            self.name = name

        def __get__(self, instance, cls):
            if instance is None:
                return self
            else:
                return instance.__dict__[self.name]

        def __set__(self, instance, value):
            print("__set__")
            if not isinstance(value, int):
                raise TypeError('Expected an int')
            instance.__dict__[self.name] = value

        def __delete__(self, instance):
            del instance.__dict__[self.name]

    class Point:
        x = Integer('x')
        y = Integer('y')

        def __init__(self, x, y):
            # self.x = Integer('x') # No! Must be a class variable
            # self.y = Integer('y')
            self.x = x
            self.y = y

    p = Point(2, 3)
    print(p.x)
    # print(p.y)
    # p.y = 5
    # p.x = 1.2
    #
    # 实例变量和类变量的区别
    # 实例变量 取得属性的值
    # print(p.x)
    # # 等同于：
    # print(Point.x.__get__(p, Point))

    # 类变量 取得属性的引用本身
    # print(Point.x)
    # 等同于：
    # print(Point.x.__get__(None, Point))


def test2():
    """
    data descriptor / dictionary / non-data descriptor 优先级
    """

    class C:
        def __init__(self, name):
            self.name = name

        def __get__(self, instance, owner):
            # print("__get__")
            if instance is None:
                # owner.__dict__[self.name] = 1111
                return self
            else:
                # setattr(instance, instance.__dict__[self.name], 9999)
                instance.__dict__.__setitem__(self.name, 9999)
                # instance.__dict__[self.name] = 9999
                return instance.__dict__[self.name]

        def __set__(self, instance, value):
            pass

    class A:
        x = C('x')
        y = C('y')

        def __init__(self):
            pass

    a = A()
    print(a.x)
    print(a.x)
    print(a.x)
    print(a.x)
    # print(A.x)
    # print(A.x)


# test2()

def test3():
    """
    类属性 / 对象属性 传递给__get__()、__set__()函数的instance变量不同。
    """

    class C:
        def __init__(self, name):
            self.name = name

        def __get__(self, instance, owner):
            if instance is None:
                print("None")
                return self
            else:
                print("instance")
                return 0

        def __set__(self, instance, value):
            pass

    class A:
        x = C('x')
        y = C('y')

        def __init__(self):
            pass

    a = A()
    print(a.x)
    print(A.x)


test3()


def test4():
    class RevealAccess(object):
        """
            A data descriptor that sets and returns values
        normally and prints a message logging their access.
        """

        def __init__(self, initval=None, name='var'):
            self.val = initval
            self.name = name

        def __get__(self, obj, objtype):
            print('Retrieving', self.name)
            return self.val

        def __set__(self, obj, val):
            print('Updating', self.name)
            self.val = val

    class MyClass(object):
        x = RevealAccess(10, 'var "x"')
        y = 5

    m = MyClass()
