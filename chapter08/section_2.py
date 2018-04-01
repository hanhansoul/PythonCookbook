# descriptor
# class decorator
# metaclass
# mixin classes
def chapter_8_13():
    """
    !!!
    8.13. Implementing a Data Model or Type System
        You want to define various kinds of data structures, but want to enforce constraints on the values that are
    allowed to be assigned to certain attributes.
    """

    def test1():
        # Base class
        class Descriptor:
            def __init__(self, name=None, **opts):
                self.name = name
                for key, value in opts.items():
                    setattr(self, key, value)

            def __set__(self, instance, value):
                instance.__dict__[self.name] = value

        # Descriptor for enforcing types
        class Typed(Descriptor):
            expected_type = type(None)

            def __set__(self, instance, value):
                if not isinstance(value, self.expected_type):
                    raise TypeError('expected ' + str(self.expected_type))
                super(Typed, self).__set__(instance, value)

        # Descriptor for enforcing values
        class Unsigned(Descriptor):
            def __set__(self, instance, value):
                if value < 0:
                    raise ValueError('Expected >= 0')
                super(Unsigned, self).__set__(instance, value)

        class MaxSized(Descriptor):
            def __init__(self, name=None, **opts):
                if 'size' not in opts:
                    raise TypeError('missing size option')
                super(MaxSized, self).__init__(name, **opts)

            def __set__(self, instance, value):
                if len(value) >= self.size:
                    raise ValueError('size must be < ' + str(self.size))
                super(MaxSized, self).__set__(instance, value)

        class Integer(Typed):
            expected_type = int

        class UnsignedInteger(Integer, Unsigned):
            pass

        class Float(Typed):
            expected_type = float

        class UnsignedFloat(Float, Unsigned):
            pass

        class String(Typed):
            expected_type = str

        class SizedString(String, MaxSized):
            pass

        class Stock:
            name = SizedString('name', size=8)
            shares = UnsignedInteger('shares')
            price = UnsignedFloat('price')

            def __init__(self, name, shares, price):
                self.name = name
                self.shares = shares
                self.price = price

        s = Stock('ACME', 50, 91.1)
        print(s.name)
        # s.shares = 75
        # s.shares = -10
        # s.price = 'a lot'
        # s.name = 'ABCDEFGHIJKLMN'
        pass

        # Class decorator to apply constraints
        def decorator_example():
            def check_attributes(**kwargs):
                def decorate(cls):
                    for key, value in kwargs.items():
                        if isinstance(value, Descriptor):
                            value.name = key
                            setattr(cls, key, value)
                        else:
                            setattr(cls, key, value(key))
                    return cls

                return decorate

            @check_attributes(name=SizedString(size=8),
                              share=UnsignedInteger,
                              price=UnsignedFloat)
            class StockDecorator:
                """
                类装饰器 & 方法装饰器
                """

                def __init__(self, name, shares, price):
                    self.name = name
                    self.shares = shares
                    self.price = price

        """
        __new__() & __init__()
        """

        # A metaclass that applies checking
        def metaclass_example():
            class checkedmeta(type):
                def __new__(cls, clsname, bases, methods):
                    for key, value in methods.items():
                        if isinstance(value, Descriptor):
                            value.name = key
                    return type.__new__(cls, clsname, bases, methods)

            class StockMetaclass(metaclass=checkedmeta):
                name = SizedString(size=8)
                shares = UnsignedInteger()
                price = UnsignedFloat()

                def __init__(self, name, shares, price):
                    self.name = name
                    self.shares = shares
                    self.price = price

        """
            class decorator approach can also be used as a replacement for mixin classes, multiple inheritance, and
        tricky use of the super() function.
        """

        def decorator_alternative():
            # Base class. Uses a descriptor to set a value
            class Descriptor:

                def __init__(self, name=None, **opts):
                    self.name = name
                    for key, value in opts.items():
                        setattr(self, key, value)

                def __set__(self, instance, value):
                    instance.__dict__[self.name] = value

            # Decorator for applying type checking
            def Typed(expected_type, cls=None):
                if cls is None:
                    return lambda cls: Typed(expected_type, cls)
                super_set = cls.__set__

                def __set__(self, instance, value):
                    if not isinstance(value, expected_type):
                        raise TypeError('expected ' + str(expected_type))
                    super_set(self, instance, value)
                    cls.__set__ = __set__
                    return cls

            # Decorator for unsigned values
            def Unsigned(cls):
                super_set = cls.__set__

                def __set__(self, instance, value):
                    if value < 0:
                        raise ValueError('Expected >= 0')
                    super_set(self, instance, value)

                cls.__set__ = __set__
                return cls

            # Decorator for allowing sized values
            def MaxSized(cls):
                super_init = cls.__init__

                def __init__(self, name=None, **opts):
                    if 'size' not in opts:
                        raise TypeError('missing size option')
                    super_init(self, name, **opts)

                cls.__init__ = __init__
                super_set = cls.__set__

                def __set__(self, instance, value):
                    if len(value) >= self.size:
                        raise ValueError('size must be < ' + str(self.size))
                    super_set(self, instance, value)

                cls.__set__ = __set__
                return cls

            # Specialized descriptors
            @Typed(int)
            class Integer(Descriptor):
                pass

            @Unsigned
            class UnsignedInteger(Integer):
                pass

            @Typed(float)
            class Float(Descriptor):
                pass

            @Unsigned
            class UnsignedFloat(Float):
                pass

            @Typed(str)
            class String(Descriptor):
                pass

            @MaxSized
            class SizedString(String):
                pass


def chapter_8_14():
    """
    8.14. Implementing Custom Containers
        You want to implement a custom class that mimics the behavior of a common built-in container type, such
    as a list or dictionary. However, you’re not entirely sure what methods need to be implemented to do it.
    """

    def test1():
        import collections
        import bisect
        class A(collections.Iterable):
            """
            support iteration ----> implements __iter__()
                The special feature about inheriting from collections.Iterable is that it ensures you implement all of
            the required special methods.
                Sequence / MutableSequence / Mapping / MutableMapping / Set / MutableSet
            """
            pass

        class SortedItems(collections.Sequence):
            def __init__(self, initial=None):
                self._items = [] if initial is None else sorted(initial)

            def __getitem__(self, index):
                print(self._items)
                return self._items[index]

            def __len__(self):
                return len(self._items)

            def add(self, item):
                bisect.insort(self._items, item)

        items = SortedItems([5, 1, 3])
        # print(list(items))
        print(items[0])
        print(items[-1])
        items.add(2)
        items.add(-10)
        print(list(items))
        print(items[1:4])

    def test2():
        import collections
        class Items(collections.MutableSequence):
            def __init__(self, initial=None):
                self._items = list(initial) if initial is None else []

            def __getitem__(self, item):
                print('Getting:', item)
                return self._items[item]

            def __setitem__(self, key, value):
                print('Setting:', key, value)
                self._items[key] = value

            def __delitem__(self, key):
                print('Deleting:', key)
                del self._items[key]

            def insert(self, key, value):
                print('Inserting:', key, value)
                self._items.insert(key, value)

            def __len__(self):
                print('Len')
                return len(self._items)

    def test3():
        import collections
        import bisect
        class A(collections.Iterable):
            """
            support iteration ----> implements __iter__()
                The special feature about inheriting from collections.Iterable is that it ensures you implement all of
            the required special methods.
                Sequence / MutableSequence / Mapping / MutableMapping / Set / MutableSet
            """
            pass

        class SortedItems(collections.Sequence):
            def __init__(self, initial=None):
                self._items = [] if initial is None else sorted(initial)

            def __getitem__(self, index):
                print(self._items)
                return self._items[index]

            def __len__(self):
                return len(self._items)

            def add(self, item):
                bisect.insort(self._items, item)

        items = SortedItems([5, 1, 3])
        # print(list(items))
        print(items[0])
        print(items[-1])
        items.add(2)
        items.add(-10)
        print(list(items))
        print(items[1:4])


def chapter_8_15():
    """
    8.15. Delegating Attribute Access
        设计模式：委托模式(Delegation) / 代理模式(Proxy)
        You want an instance to delegate attribute access to an internally held instance possibly as an alternative
    to inheritance or in order to implement a proxy.
        if there are many methods to delegate, an alternative approach is to define the __getattr__() method
        __getattr__() gets called if code tries to access an attribute that doesn’t exist.
        Delegation is sometimes used as an alternative to inheritance.

        DELEGATION
        This use of delegation is often useful in situations where direct inheritance might not make much sense
    or where you want to have more control of the relationship between objects
        NOTE
        1. __getattr__()只有在代理类中的不存在该属性时才会触发；
        2. __setattr__()和__delattr__()需要对代理类和被代理的类中的属性进行进一步的区分和
            处理，一般而言，代理类只处理public属性；
        3. __getattr__()对大多数__XXXX__()形式的方法不起作用。
    """

    def test1():
        class A:
            def spam(self, x):
                pass

            def foo(self):
                pass

        class B:
            def __init__(self):
                self._a = A()

            def spam(self, x):
                return self._a.spam(x)

            def foo(self):
                return self._a.foo()

            def bar(self):
                pass

        class NewB:
            def __init__(self):
                self._a = A()

            def bar(self):
                pass

            def __getattr__(self, name):
                return getattr(self._a, name)

    def test2():
        # A proxy class that wraps around another object, but
        # exposes its public attributes
        class Proxy:
            def __init__(self, obj):
                self._obj = obj

            def __getattr__(self, name):
                print('getattr:', name)
                return getattr(self._obj, name)

            def __setattr__(self, name, value):
                if name.startswith('_'):
                    super().__setattr__(name, value)
                else:
                    print('setattr:', name, value)
                    setattr(self._obj, name, value)

            def __delattr__(self, name):
                if name.startswith('_'):
                    super().__delattr__(name)
                else:
                    print('delattr:', name)
                    delattr(self._obj, name)

        class Spam:
            def __init__(self, x):
                self.x = x

            def bar(self, y):
                print('Spam.bar:', self.x, y)

        s = Spam(2)
        p = Proxy(s)
        print(p.x)
        p.bar(3)
        p.x = 37

    def test3():
        class ListLike:
            def __init__(self):
                self._items = []

            def __getattr__(self, item):
                return getattr(self._items, item)

        a = ListLike()
        a.append(2)
        a.insert(0, 1)
        a.sort()
        # len(a)
        # print(a[0])

        """
            2. __setattr__()和__delattr__()需要对代理类和被代理的类中的属性进行进一步的区分和处理，一般而言，代理类只处理public属性；
            3. __getattr__()对大多数__XXXX__()形式的方法不起作用。
        """

        class A:
            def spam(self, x):
                pass

            def foo(self):
                pass

        class B:
            def __init__(self):
                self._a = A()

            def spam(self, x):
                return self._a.spam(x)

            def foo(self):
                return self._a.foo()

            def bar(self):
                pass

        class NewB:
            def __init__(self):
                self._a = A()

            def bar(self):
                pass

            def __getattr__(self, name):
                return getattr(self._a, name)

        # A proxy class that wraps around another object, but exposes its public attributes
        class Proxy:
            def __init__(self, obj):
                self._obj = obj

            def __getattr__(self, name):
                print('getattr:', name)
                return getattr(self._obj, name)

            def __setattr__(self, name, value):
                if name.startswith('_'):
                    super().__setattr__(name, value)
                else:
                    print('setattr:', name, value)
                    setattr(self._obj, name, value)

            def __delattr__(self, name):
                if name.startswith('_'):
                    super().__delattr__(name)
                else:
                    print('delattr:', name)
                    delattr(self._obj, name)

        class Spam:
            def __init__(self, x):
                self.x = x

            def bar(self, y):
                print('Spam.bar:', self.x, y)

        s = Spam(2)
        p = Proxy(s)
        print(p.x)
        p.bar(3)
        p.x = 37


def chapter_8_16():
    """
    8.16. Defining More Than One Constructor in a Class
        @classmethod
        You’re writing a class, but you want users to be able to create instances in more than the one way
    provided by __init__().
        在c++和Java中可以通过重载构造器实现不同的构造方法，但python中不可行，因此，类方法提供了一种实现多种构造器的方法。
        我们想写一些仅仅与类交互而不是和实例交互的方法，写一个只在类中运行而不在实例中运行的方法。
        类方法可以被继承
    ======================
        class A:
            def __init__(self, x):
                self.x = x
            @classmethod
            def fun(cls, y):
                return cls.x + y

        不管这个方式是从实例调用还是从类调用，类方法的第一个参数cls把类传递过来.
    ======================
    """
    def test1():
        import time
        class Date:
            def __init__(self, year, month, day):
                self.year = year
                self.month = month
                self.day = day

            @classmethod
            def today(cls):
                t = time.localtime()
                return cls(t.tm_year, t.tm_mon, t.tm_mday)

        a = Date(2010, 10, 1)
        b = Date.today()


    def classmethod_and_staticmethod():
        class A:
            x = 5

            def __init__(self, x):
                self.x = x

            @classmethod
            def class_fun(cls, y):
                return cls.x + y

            @staticmethod
            def static_fun():
                print('call static fun.')

        a = A(10)
        print(a.class_fun(30))
        print(A.class_fun(20))
        A.x = 100
        print(A.class_fun(20))
        A.static_fun()


# __new__()
def chapter_8_17():
    """
    8.17. Creating an Instance Without Invoking init
        __new__()
        You need to create an instance, but want to bypass the execution of the __init__() method for some reason.
        Use __new__ when you need to control the creation of a new instance. Use __init__ when you need to control
    the initialization of a new instance.
        __new__ is the first step of instance creation. It's called first, and is responsible for returning a new
    instance of your class. In contrast, __init__ doesn't return anything; it's only responsible for initializing
    the instance after it's been created.
        In general, you shouldn't need to override __new__ unless you're subclassing an immutable type like str,
    int, unicode or tuple. The return value of __new__() should be the new object instance (usually an instance of cls).

        Called to create a new instance of class cls. __new__() is a static method (special-cased so you need not
    declare it as such) that takes the class of which an instance was requested as its first argument.

        __new__ is static class method, while __init__ is instance method.  __new__ has to create the instance
    first, so __init__ can initialize it. Note that __init__ takes self as parameter. Until you create instance
    there is no self.

        1. __new__ is for object creation
        2. __init__ is for object initialization
        3. __new__ is invoked before __init__ as __new__ returns a new instance and __init__ invoked afterwards
        to initialize inner state.
        4. __new__ is good for immutable object as they cannot be changed once they are assigned. So we can
        return new instance which has new state.
        5. We can use __new__ and __init__ for both mutable object as its inner state can be changed.

        在classmethod的构造器中使用__new__()，可以先创建初始化
    """

    class Date:
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

    d = Date.__new__(Date)
    data = {'year': 2020, 'month': 10, 'day': 15}
    for key, value in data.items():
        setattr(d, key, value)
    print(d.year)


def chapter_8_18():
    """
    8.18. Extending Classes with Mixins

    """
