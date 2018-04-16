# metaclass


def chapter_9_13():
    """
    9.13. Using a Metaclass to Control Instance Creation
        You want to change the way in which instances are created in order to implement singletons,
    caching, or other similar features.

    metaclass
    修改实例创建的方式，以实现单例模式，缓存或其他模式。
    创建一个metaclass并重新实现__call__()方法。
    """

    def test1():
        """
        无人可以创建类的实例
        """

        class NoInstance(type):
            def __call__(self, *args, **kwargs):
                raise TypeError("Can't instantiate directly")

        class Spam(metaclass=NoInstance):
            @staticmethod
            def grok(x):
                print('Spam.grok')

        Spam.grok(10)
        # wrong
        # Spam()

    def test2():
        """
        单例模式
        """

        # Singleton
        class Singleton(type):
            def __init__(self, *args, **kwargs):
                self.__instance = None
                super().__init__(*args, **kwargs)

            def __call__(self, *args, **kwargs):
                if self.__instance is None:
                    self.__instance = super(Singleton, self).__call__(*args, **kwargs)
                    return self.__instance
                else:
                    return self.__instance

        class SpamSingle(metaclass=Singleton):
            def __init__(self):
                print('Creating Spam')

        a = SpamSingle()
        b = SpamSingle()
        c = SpamSingle()
        print(a is b)
        print(b is c)

    def test3():
        import weakref

        class Cached(type):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.__cache = weakref.WeakValueDictionary()

            def __call__(self, *args, **kwargs):
                if args in self.__cache:
                    return self.__cache[args]
                else:
                    obj = super().__call__(*args)
                    self.__cache[args] = obj
                    return obj

        class SpamCached(metaclass=Cached):
            def __init__(self, name):
                print('Creating Spam({!r})'.format(name))
                self.name = name

        a = SpamCached('Guido')
        b = SpamCached('Diana')
        c = SpamCached('Guido')
        print(a is b)
        print(a is c)

    def test4():
        """
        不使用metaclass实现单例模式
        """

        class _Spam:
            def __init__(self):
                print("Creating Spam")

        _spam_instance = None

        def Spam():
            global _spam_instance
            if _spam_instance is not None:
                return _spam_instance
            else:
                _spam_instance = _Spam()
                return _spam_instance

    # TODO metaclass详解 test5()/test6()
    # https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python

    def test5():
        """
        metaclass
        """

        # the metaclass will automatically get passed the same argument
        # that you usually pass to `type`
        def upper_attr(future_class_name, future_class_parents, future_class_attr):
            """
              Return a class object, with the list of its attribute turned
              into uppercase.
            """
            # pick up any attribute that doesn't start with '__' and uppercase it
            uppercase_attr = {}
            for name, val in future_class_attr.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val

            # let `type` do the class creation
            return type(future_class_name, future_class_parents, uppercase_attr)

        class Foo(metaclass=upper_attr):  # global __metaclass__ won't work with "object" though
            # but we can define __metaclass__ here instead to affect only this class
            # and this will work with "object" children
            bar = 'bip'

        print(hasattr(Foo, 'bar'))
        # Out: False
        print(hasattr(Foo, 'BAR'))
        # Out: True

        f = Foo()
        print(f.BAR)
        # Out: 'bip'

    def test6():
        class UpperAttrMetaClass(type):
            def __new__(cls, clsname, bases, d):
                uppercase_attr = dict((name.upper(), val) for name, val in d.items() if not name.startswith('__'))
                # return super(UpperAttrMetaClass, cls).__new__(cls, clsname, bases, uppercase_attr)
                return super().__new__(cls, clsname, bases, uppercase_attr)

        class Foo(metaclass=UpperAttrMetaClass):
            bar = 'bip'

        print(hasattr(Foo, 'bar'))
        print(hasattr(Foo, 'BAR'))

        f = Foo()
        # print(f.BAR)


def chapter_9_14():
    """
    9.14. Capturing Class Attribute Definition Order
        metaclass
        You want to automatically record the order in which attributes and methods are defined
    inside a class body so that you can use it in various operations (e.g., serializing, mapping
    to databases, etc.).

    __prepare__()方法会在类定义开始时被调用，类名和其基类会被传递给该方法。该方法会返回一个map对象作为类的命名空间__dict__。
    """
    from collections import OrderedDict

    class Typed:
        _expected_type = type(None)

        def __init__(self, name=None):
            self.name = name

        def __set__(self, instance, value):
            if not isinstance(value, self._expected_type):
                raise TypeError('Expected ' + str(self._expected_type))
            instance.__dict__[self._name] = value

    class Integer(Typed):
        _expected_type = int

    class Float(Typed):
        _expected_type = float

    class String(Typed):
        _expected_type = str

    class OrderedMeta(type):
        def __new__(cls, clsname, bases, clsdict):
            # d = dict(clsdict)
            d = clsdict
            order = []
            for name, value in clsdict.items():
                if isinstance(value, Typed):
                    value._name = name
                    order.append(name)
            d['_order'] = order
            return type.__new__(cls, clsname, bases, d)

        @classmethod
        def __prepare__(cls, clsname, bases):
            return OrderedDict()

    class Structure(metaclass=OrderedMeta):
        def as_csv(self):
            return ','.join(str(getattr(self.name)) for name in self._order)

    class Stock(Structure):
        name = String()
        shares = Integer()
        price = Float()

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

    s = Stock('G00G', 100, 490.1)
    print(s.name)
    print(s.as_csv())


def chapter_9_15():
    """
    为metaclass类提供可选的参数。
    """
