def chapter_8_1():
    """
    8.1. Changing the String Representation of Instances
        __str__() & __repr__()
        You want to change the output produced by printing or viewing instances to something
    more sensible.
        The __repr__() method returns the code representation of an instance, and is usually the text you would
    type to re-create the instance. The built-in repr() function returns this text, as does the interactive
    interpreter when inspecting values.
        The __str__() method converts the instance to a string, and is the output produced by the str() and
    print() functions.

        Specifically, the special !r formatting code indicates that the output of __repr__() should be used
    instead of __str__(), the default.
    """

    class Pair:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return 'Pair({0.x!r}, {0.y!r})'.format(self)

        def __str__(self):
            return '({0.x!s}, {0.y!s})'.format(self)

    p = Pair(1, 3)
    print(repr(p))
    print(p)
    print(str(p))

    """
    It is standard practice for the output of __repr__() to produce text such that eval(repr(x)) == x.
    """

    e = eval(repr(p))
    print(e)


def chapter_8_2():
    """
    8.2. Customizing String Formatting
    You want an object to support customized formatting through the format() function and string method.
    To customize string formatting, define the __format__() method on a class.
    重载了的类的__format__()函数会在调用format()函数时被调用
    """
    _formats = {
        'ymd': '{d.year}-{d.month}-{d.day}',
        'mdy': '{d.month}/{d.day}/{d.year}',
        'dmy': '{d.day}/{d.month}/{d.year}'
    }

    from datetime import date

    class Date:
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

        def __format__(self, code):
            if code == '':
                code = 'ymd'
            fmt = _formats[code]
            return fmt.format(d=self)

    d = Date(2012, 12, 21)
    print(format(d))
    print(format(d, 'mdy'))
    print('The date is {:ymd}'.format(d))
    print('The date is {:mdy}'.format(d))


def chapter_8_3():
    """
    8.3. Making Objects Support the Context-Management Protocol
        实现类的__enter__() / __exit__()方法，使其支持context manager。
        当进入with语句块时，__enter__()被调用，其返回值将传递给as后的变量。
        当离开with语句块时，__exit__()被调用，可用于关闭和清理工作。
        You want to make your objects support the context-management protocol (the with statement).
        In order to make an object compatible with the with statement, you need to implement __enter__() and __exit__()
    methods.
        The main principle behind writing a context manager is that you’re writing code that’s meant to surround
    a block of statements as defined by the use of the with statement. When the with statement is first encountered,
    the __enter__() method is triggered. The return value of __enter__() (if any) is placed into the variable
    indicated with the as qualifier. Afterward, the statements in the body of the with statement execute. Finally,
    the __exit__() method is triggered to clean up.
        Context managers are most commonly used in programs that need to manage resources such as files, network
    connections, and locks.
    """
    from socket import socket, AF_INET, SOCK_STREAM
    class LazyConnection:
        def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
            self.address = address
            self.family = family
            self.type = SOCK_STREAM
            self.sock = None

        def __enter__(self):
            if self.sock is not None:
                raise RuntimeError('Already connected')
            self.sock = socket(self.family, self.type)
            self.sock.connect(self.address)
            return self.sock

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.sock.close()
            self.sock = None

    from functools import partial
    conn = LazyConnection(('www.python.org', 80))
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)


def chapter_8_4():
    """
    8.4. Saving Memory When Creating a Large Number of Instances
        __slots__
        Your program creates a large number (e.g., millions) of instances and uses a large amount of memory.
        For classes that primarily serve as simple data structures, you can often greatly reduce the memory footprint
    of instances by adding the __slots__ attribute to the class definition.
        When you define __slots__, Python uses a much more compact internal representation for instances. Instead of
    each instance consisting of a dictionary, instances are built around a small fixed-sized array, much like a tuple
    or list. Attribute names listed in the __slots__ specifier are internally mapped to specific indices within this
    array. A side effect of using slots is that it is no longer possible to add new attributes to instances. You are
    restricted to only those attribute names listed in the __slots__ specifier.
    """

    class Date:
        __slots__ = ['year', 'month', 'day']

        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day


def chapter_8_5():
    """
    !!!
    8.5. Encapsulating Names in a Class
        You want to encapsulate “private” data on instances of a class, but are concerned about Python’s lack of
    access control.
        The first convention is that any name that starts with a single leading underscore (_) should always be
    assumed to be internal implementation. Python doesn’t actually prevent someone from accessing internal names.
        The use of double leading underscores (__) causes the name to be mangled to something else. Specifically, the
    private attributes in the preceding class get renamed to _B__private and _B__private_method, respectively. Such
    attributes cannot be overridden via inheritance.
        It should be noted, too, that the use of the leading underscore is also used for module names and module-level
    functions.

        It should also be noted that sometimes you may want to define a variable that clashes with the name of a
    reserved word. For this, you should use a single trailing underscore. For example:
        lambda_ = 2.0 # Trailing _ to avoid clash with lambda keyword
    The reason for not using a leading underscore here is that it avoids confusion about the intended usage (i.e.,
    the use of a leading underscore could be interpreted as a way to avoid a name collision rather than as an
    indication that the value is private).

    """

    class B:
        _pvt_num = 0
        __pvt_num = 10

        def __init__(self):
            print('B')

        def __print(self):
            print('__print B class')

        def _print(self):
            print('_print B class')

        def public_print(self):
            print('public print B class')

    class C(B):
        def __init__(self):
            print('C')

        def __print(self):  # _C__print()
            print('__print C class')

        def _print(self):
            print('_print C class')

        def fun(self):
            super(C, self)._B__print()
            super(C, self)._print()
            super(C, self).public_print()
            super().public_print()
            self._C__print()
            self.__print()
            self._print()
            print(super(C, self)._pvt_num)
            print(super(C, self)._B__pvt_num)

    c = C()
    c._C__print()
    # error! function name is mangled
    # c.__print()
    # __print() -> _C__print() but private function should not be called outside class
    c._C__print()
    c.fun()


def chapter_8_6():
    """
    !!!
    @property

    8.6. Creating Managed Attributes
        You want to add extra processing (e.g., type checking or validation) to the getting or setting of an
    instance attribute.
        A simple way to customize access to an attribute is to define it as a “property.”

        Don’t write properties that don’t actually add anything extra like this.
        1. it makes your code more verbose and confusing to others.
        2. it will make your program run a lot slower.
        3. it offers no real design benefit.

        Don’t write Python code that features a lot of repetitive property definitions, there are much better ways
    to achieve the same thing using descriptors or closures.
    """

    class Person:
        """
            In the class, there are three related methods, all of which must have the same name. The first method
        is a getter function, and establishes first_name as being a property. The other two methods attach optional
        setter and deleter functions to the first_name property. It’s important to stress that the @first_name.setter
        and @first_name.deleter decorators won’t be defined unless first_name was already established as a property
        using @property.

            A critical feature of a property is that it looks like a normal attribute, but access automatically
        triggers the getter, setter, and deleter methods.
        """

        def __init__(self, first_name):
            """
                __init__() method sets self.first_name instead of self._first_name.
                By setting self.first_name, the set operation uses the setter method (as opposed to bypassing it by
            accessing self._first_name).
            """
            self.first_name = first_name

        @property
        def first_name(self):
            print("getter")
            return self._first_name

        @first_name.setter
        def first_name(self, value):
            print("setter")
            if not isinstance(value, str):
                raise TypeError("Expected a string")
            self._first_name = value

        @first_name.deleter
        def first_name(self):
            print("delete")
            raise AttributeError("Can't delete attribute")

    a = Person('GUI')
    print(a.first_name)
    a.first_name = 10
    del a.first_name

    import math

    class Circle:
        """
            Properties can also be a way to define computed attributes. These are attributes that are not actually
        stored, but computed on demand.
            The use of properties results in a very uniform instance interface in that radius, area, and perimeter
        are all accessed as simple attributes, as opposed to a mix of simple attributes and method calls.
        """

        def __init__(self, radius):
            self.radius = radius

        @property
        def area(self):
            return math.pi * self.radius ** 2

        @property
        def perimeter(self):
            return 2 * math.pi * self.radius


def chapter_8_7():
    """
    !!!
    8.7. Calling a Method on a Parent Class
        super() https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
        MRO C3 https://www.python.org/download/releases/2.3/mro/
        types and objects http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html
        http://python.jobbole.com/85685/

        super([type[, object-or-type]]): Return a proxy object that delegates method calls to a parent or sibling
    class of type. The __mro__ attribute of the type lists the method resolution search order used by both getattr()
    and super(). The attribute is dynamic and can change whenever the inheritance hierarchy is updated.
        super(type, obj) || super(type, type2)
        If the second argument is omitted, the super object returned is unbound. If the second argument is an
    object, isinstance(obj, type) must be true. If the second argument is a type, issubclass(type2, type) must be
    true (this is useful for classmethods).
        1. There are two typical use cases for super. In a class hierarchy with single inheritance, super can be used
    to refer to parent classes without naming them explicitly, thus making the code more maintainable.
        2. The second use case is to support cooperative multiple inheritance in a dynamic execution environment. This
    use case is unique to Python and is not found in statically compiled languages or languages that only support
    single inheritance. This makes it possible to implement “diamond diagrams” where multiple base classes implement
    the same method. Good design dictates that this method have the same calling signature in every case (because the
    order of calls is determined at runtime, because that order adapts to changes in the class hierarchy, and because
    that order can include sibling classes that are unknown prior to runtime).
        It's been noted that in Python 3.0+ you can use super().__init__()

        isinstance(): Return true if the object argument is an instance of the classinfo argument,
    or of a (direct, indirect or virtual) subclass thereof.
        issubclass(): Return true if class is a subclass (direct, indirect or virtual) of classinfo.
    A class is considered a subclass of itself.

        You want to invoke a method in a parent class in place of a method that has been overridden in a subclass.
        A very common use of super() is in the handling of the __init__() method to make sure that parents are
    properly initialized.
    """

    class A:
        def spam(self):
            print('A.spam')

    class B(A):
        def spam(self):
            print('B.spam')
            super().spam()  # Call parent spam()

    b = B()
    b.spam()

    class Base:
        def __init__(self):
            super().__init__()
            print('Base init')

    class C(Base):
        def __init__(self):
            super().__init__()
            print('C init')

    class D(Base):
        def __init__(self):
            super().__init__()
            print('D init')

    class E(C, D):
        def __init__(self):
            super().__init__()
            print('E init')

    e = E()
    """
    error!
    class F(Base):
        pass

    class G(Base, F):
        pass

    g = G()
    """


def chapter_8_8():
    """
    8.8. Extending a Property in a Subclass
        Within a subclass, you want to extend the functionality of a property defined in a parent class.
    """

    def test1():
        class Person:
            def __init__(self, name):
                self.name = name

            @property
            def name(self):
                return self._name

            @name.setter
            def name(self, value):
                if not isinstance(value, str):
                    raise TypeError("Expected a string")
                self._name = value

            @name.deleter
            def name(self):
                raise AttributeError("Can't delete attribute")

        class SubPerson(Person):
            """
                Within each method, super() is used to call the previous implementation. The use of
            super(SubPerson, SubPerson).name.__set__(self, value) in the setter function is no mistake. To delegate to
            the previous implementation of the setter, control needs to pass through the __set__() method of the
            previously defined name property. However, the only way to get to this method is to access it as a class
            variable instead of an instance variable. This is what happens with the super(SubPerson, SubPerson) operation.
            """

            @property
            def name(self):
                print('Getting name')
                return super().name

            @name.setter
            def name(self, value):
                print('Setting name to', value)
                # print(super())
                # print(super(Person, self))
                # print(super(SubPerson, SubPerson))
                super(SubPerson, SubPerson).name.__set__(self, value)
                # super(SubPerson, self).name.__set__(self, value)

            @name.deleter
            def name(self):
                print('Deleting name')
                super(SubPerson, SubPerson).name.__delete__(self)

            def super_test(self):
                print(super())
                print(super(SubPerson, self))
                print(super(SubPerson, SubPerson))

        class SubPersonPart(Person):
            @Person.name.getter
            def name(self):
                print('Getting name')
                return super().name

            @Person.name.setter
            def name(self, value):
                print('Setting name to', value)
                super(SubPersonPart, SubPersonPart).name.__set__(self, value)

        s = SubPerson('GUI')
        print(s.name)
        s.name = 'LAR'
        s.name = 42

    def super_test():
        class Foo:
            def __init__(self):
                print('Foo')

        class Bar(Foo):
            def __init__(self):
                print('Bar')

        class Dee(Bar):
            def __init__(self):
                """
                    super(type, object-or-type)通过super中的__set__方法，将type的MRO列表顺序中的第一个父类绑定在object-or-type上，
                并通过super()中的__get__和__set__方法进行访问，返回一个super类型的对象。实例化时第一个参数是一个type，第二个参数可以是
                type的instance，也可以是type的subclass。
                """
                m = super(Dee, self)
                print(m)
                print(m.__class__)
                m.fun()
                # super(Dee, self).__init__()
                # print()
                print('Dee')

        d = Dee()


# descriptor
def chapter_8_9():
    """
    8.9. Creating a New Kind of Class or Instance Attribute
        descriptor ???
        https://docs.python.org/2/howto/descriptor.html
        You want to create a new kind of instance attribute type with some extra functionality, such as type checking.
        If you want to create an entirely new kind of instance attribute, define its functionality in the form of a
    descriptor class.
        Descriptors provide the underlying magic for most of Python’s class features, including @classmethod,
    @staticmethod, @property, and even the __slots__ specification.

        使用descriptor和@property的取舍
        It should be stressed that you would probably not write a descriptor if you simply want to customize the
    access of a single attribute of a specific class. For that, it’s easier to use a property instead.
    """

    # Descriptor attribute for an integer type-checked attribute
    class Integer:
        """
            A descriptor is a class that implements the three core attribute access operations (get, set, and delete)
        in the form of __get__(), __set__(), and __delete__() special methods. These methods work by receiving an
        instance as input. The underlying dictionary of the instance is then manipulated as appropriate.
        """

        def __init__(self, name):
            self.name = name

        def __get__(self, instance, cls):
            if instance is None:
                return self
            else:
                return instance.__dict__[self.name]

        def __set__(self, instance, value):
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
    print(p.y)
    p.y = 5
    p.x = 1.2

    """
        Descriptors are often just one component of a larger programming framework involving decorators or metaclasses.
    As such, their use may be hidden just barely out of sight. As an example, here is some more advanced
    descriptor-based code involving a class decorator.
    """

    # Descriptor for a type-checked attribute
    class Typed:
        def __init__(self, name, expected_type):
            self.name = name
            self.expected_type = expected_type

        def __get__(self, instance, cls):
            if instance is None:
                return self
            else:
                return instance.__dict__[self.name]

        def __set__(self, instance, value):
            if not isinstance(value, self.expected_type):
                raise TypeError('Expected ' + str(self.expected_type))
            instance.__dict__[self.name] = value

        def __delete__(self, instance):
            del instance.__dict__[self.name]

        # Class decorator that applies it to selected attributes
        def typeassert(**kwargs):
            def decorate(cls):
                for name, expected_type in kwargs.items():
                    # Attach a Typed descriptor to the class
                    setattr(cls, name, Typed(name, expected_type))
                return cls

            return decorate

        # Example use
        @typeassert(name=str, shares=int, price=float)
        class Stock:
            def __init__(self, name, shares, price):
                self.name = name
                self.shares = shares
                self.price = price


# descriptor
def chapter_8_10():
    """
    8.10. Using Lazily Computed Properties
        计算一次，永久保存的只读属性。
        You’d like to define a read-only attribute as a property that only gets computed on access. However,
    once accessed, you’d like the value to be cached and not recomputed on each access.
        An efficient way to define a lazy attribute is through the use of a descriptor class
    """

    class LazyProperty:
        def __init__(self, func):
            self.func = func

        def __get__(self, instance, owner):
            if instance is None:
                return self
            else:
                print('__get__')
                value = self.func(instance)
                # setattr创建新的属性 self.func.__name__
                setattr(instance, self.func.__name__, value)
                return value

    import math
    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @LazyProperty
        def area(self):
            print('Computing area')
            return math.pi * self.radius ** 2

        @LazyProperty
        def perimeter(self):
            print('Computing perimeter')
            return 2 * math.pi * self.radius

    c = Circle(4.0)
    print(c.radius)
    print(c.area)
    print(c.area)
    print(c.perimeter)
    print(c.perimeter)


def chapter_8_11():
    """
    8.11. Simplifying the Initialization of Data Structures
        setattr()
        You are writing a lot of classes that serve as data structures, but you are getting tired of
    writing highly repetitive and boilerplate __init__() functions.
    """

    class Structure:
        # Class variable that specifies expected fields
        _fields = []

        def __init__(self, *args):
            if len(args) != len(self._fields):
                raise TypeError('Expected {} arguments'.format(len(self._fileds)))
            # Set the arguments
            for name, value in zip(self._fields, args):
                setattr(self, name, value)

    class StructureKeyWords:
        # support keyword arguments
        _fields = []

        def __init__(self, *args, **kwargs):
            if len(args) > len(self._fields):
                raise TypeError('Expected {} arguments'.format(len(self._fields)))

            # Set all of the positional arguments
            for name, value in zip(self._fields, args):
                setattr(self, name, value)

            # Set the remaining keyword arguments
            for name in self._fields[len(args):]:
                setattr(self, name, kwargs.pop(name))

            # Check for any remaining unknown arguments
            if kwargs:
                raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))

    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x', 'y']

    import math

    class Circle(Structure):
        _fields = ['radius']

        def area(self):
            return math.pi * self.radius ** 2

    s = Stock('ACME', 50, 100)
    p = Point(4, 3)
    c = Circle(1.5)


def chapter_8_12():
    """
    8.12. Defining an Interface or Abstract Base Class
        abc module
        You want to define a class that serves as an interface or abstract base class from which you can perform
    type checking and ensure that certain methods are implemented in subclasses.
        To define an abstract base class, use the abc module. A major use of abstract base classes is in code that
    wants to enforce an expected programming interface. ABCs allow other classes to be registered as implementing the
    required interface.
        @abstractmethod can also be applied to static methods, class methods, and properties. @abstractmethod
    appears immediately before the function definition.
    """

    from abc import ABCMeta, abstractmethod
    import io

    class IStream(metaclass=ABCMeta):
        @abstractmethod
        def read(self, maxbytes=-1):
            pass

        @abstractmethod
        def write(self, data):
            pass

    IStream.register(io.IOBase)
