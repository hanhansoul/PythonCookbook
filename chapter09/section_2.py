exec_chpt = 0


def chapter_9_13():
    """
    9.13. Using a Metaclass to Control Instance Creation
        You want to change the way in which instances are created in order to implement singletons,
    caching, or other similar features.

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

def chapter_9_14():
    """
    9.14. Capturing Class Attribute Definition Order
        metaclass
        You want to automatically record the order in which attributes and methods are defined
    inside a class body so that you can use it in various operations (e.g., serializing, mapping
    to databases, etc.).
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

    class orderedMeta(type):
        def __new__(cls, clsname, bases, clsdict):
            d = dict(clsdict)
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


exec_chpt = chapter_9_14

exec_chpt()
