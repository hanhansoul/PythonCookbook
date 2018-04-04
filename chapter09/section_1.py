# decorator
def chapter_9_1():
    """
    9.1. Putting a Wrapper Around a Function
    decorator
    You want to put a wrapper layer around a function that adds extra
    processing (e.g., logging, timing, etc.).

    @staticmethod
    @classmethod
    @property

    @staticmethod / @classmethod 的区别
    """
    import time
    from functools import wraps

    def timethis(func):
        """
        Decorator that reports the execution time.
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(func.__name__, end - start)
            return result

        return wrapper

    @timethis
    def countdown(n):
        print(n)
        while n > 0:
            n -= 1

    countdown(100000)
    countdown(10000000)

    class A:
        @classmethod
        def method_deco(cls):
            pass

        # Equivalent definition of a class method
        def method_origin(cls):
            pass

        method_origin = classmethod(method_origin)


def chapter_9_2():
    """
    9.2. Preserving Function Metadata When Writing Decorators
        @wraps
        You’ve written a decorator, but when you apply it to a function, important metadata such as the name, doc
    string, annotations, and calling signature are lost.

    @wraps会将被包装函数的__name__，__doc__，__annotations__等属性传递返回的包装函数。
    同时，被包装函数可以通过__wrapped__()直接调用。
    """
    pass


def chapter_9_3():
    """
    9.3. Unwrapping a Decorator
        A decorator has been applied to a function, but you want to “undo” it, gaining access to the original
    unwrapped function.
        Assuming that the decorator has been implemented properly using @wraps (see Recipe 9.2), you can usually
    gain access to the original function by accessing the __wrapped__ attribute
        This recipe only works if the implementation of a decorator properly copies metadata using @wraps from
    the functools module or sets the __wrapped__ attribute directly. If multiple decorators have been applied to
    a function, the behavior of accessing __wrapped__ is currently undefined and should probably be avoided.
    In Python 3.3, it bypasses all of the layers. In Python3.5, NOT !!!

    通过__wrapped__属性可以获取原始的被包装函数。
    """
    from functools import wraps

    def decorator1(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)

        return wrapper

    def decorator2(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)

        return wrapper

    @decorator1
    @decorator2
    def add(x, y):
        print(x + y)

    add(2, 3)
    add.__wrapped__(2, 3)
    add.__wrapped__.__wrapped__(2, 3)


def chapter_9_4():
    """
    9.4. Defining a Decorator That Takes Arguments
        You want to write a decorator function that takes arguments.
        Writing a decorator that takes arguments is tricky because of the underlying calling sequence involved.
        ====================
        @decorator(x, y, z)
        def func(a, b):
            pass
        ====================
        def func(a, b):
            pass

        func = decorator(x, y, z)(func)
        ====================

        在包装函数的最外层再添加一层函数传入参数，在包装函数内可以直接调用这些参数。
    """

    def test1():
        from functools import wraps
        import logging

        def logged(level, name=None, message=None):
            '''
                Add logging to a function. level is the logging level, name is the logger name, and message is the log
            message. If name and message aren't specified, they default to the function's module and name.
            '''

            def decorate(func):
                logname = name if name else func.__module__
                log = logging.getLogger(logname)
                logmsg = message if message else func.__name__

                @wraps(func)
                def wrapper(*args, **kwargs):
                    log.log(level, logmsg)
                    return func(*args, **kwargs)

                return wrapper

            return decorate

        @logged(logging.DEBUG)
        def add(x, y):
            return x + y

        @logged(logging.CRITICAL, 'example')
        def spam():
            print('Spam!')

    def test2():
        from functools import wraps

        def outter(x, y, z):
            def decorator(func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                    print(x, y, z, sep=" ")
                    return func(*args, **kwargs)

                return wrapper

            return decorator

        @outter(1, 2, 3)
        def func(a, b):
            print(a + b)

        func(1, 2)

        def func_no_decorator(a, b):
            print(a + b)

        f = outter(1, 2, 3)(func_no_decorator)
        f(1, 2)


def chapter_9_5():
    """
    9.5. Defining a Decorator with User Adjustable Attributes
        functools.partial()
        Return a new partial object which when called will behave like func called with the positional arguments
    args and keyword arguments keywords. If more arguments are supplied to the call, they are appended to args. If
    additional keyword arguments are supplied, they extend and override keywords.
        函数在执行时，要带上所有必要的参数进行调用。然后，有时参数可以在函数被调用之前提前获知。这种情况下，一个函数有一
    个或多个参数预先就能用上，以便函数能用更少的参数进行调用。
    ==================================
    import functools
    def add(a, b):
        return a + b

    add(4, 2)   # 6
    plus3 = functools.partial(add, 3)
    plus5 = functools.partial(add, 5)
    plus3(4)    # 7
    plus3(7)    # 10
    plus5(10)   # 15
    ==================================

        You want to write a decorator function that wraps a function, but has user adjustable attributes that can be
    used to control the behavior of the decorator at runtime.
        Using accessor functions that change internal variables through the use of nonlocal variable declarations, the
    accessor functions are then attached to the wrapper function as function attributes
    """

    def test1():
        from functools import wraps, partial
        import logging

        def attach_wrapper(obj, func=None):
            if func is None:
                return partial(attach_wrapper, obj)
            setattr(obj, func.__name__, func)
            return func

        # def attach_wrapper(obj):
        #     def inner(func):
        #         setattr(obj, func.__name__, func)
        #         return func
        #     return inner

        def logged(level, name=None, message=None):
            def decorate(func):
                logname = name if name else func.__name__
                log = logging.getLogger(logname)
                logmsg = message if message else func.__name__

                @wraps(func)
                def wrapper(*args, **kwargs):
                    log.log(level, logmsg)
                    return func(*args, **kwargs)

                """
                @attach_wrapper(wrapper)将set_level和set_message绑定为wrapper的属性
                
                attach_wrapper(wrapper, func=None)
                ==> partial(attach_wrapper, wrapper)
                ==> attach_wrapper(wrapper, func=set_level)
                ==> setattr(wrapper, set_level.__name__, set_level)
                ==> return set_level

                set_level = attach_wrapper(wrapper, func=None)(wrapper, func=set_level)
                
                nonlocal / global
                """

                @attach_wrapper(wrapper)
                def set_level(newlevel):
                    nonlocal level
                    level = newlevel

                @attach_wrapper(wrapper)
                def set_message(newmsg):
                    nonlocal logmsg
                    logmsg = newmsg

                return wrapper

            return decorate

        @logged(logging.DEBUG)
        def add(x, y):
            print(x + y)

        @logged(logging.CRITICAL, 'example')
        def spam():
            print('Spam!')

        logging.basicConfig(level=logging.DEBUG)
        add(2, 3)
        add.set_message('Add called')
        add(2, 3)
        add.set_level(logging.WARNING)
        add(2, 3)

    def test2():
        pass

    def test3():
        from functools import partial

        def attach_wrapper(obj, func=None):
            if func is None:
                return partial(attach_wrapper, obj)
            setattr(obj, func.__name__, func)
            return func

        def wrapper():
            print("wrapper")

        @attach_wrapper(wrapper)
        def ff():
            print("ff")

        a = 1

        def g(obj1, obj2):
            return obj1 + obj2

        gg = partial(g, obj2=a)

        gg(2)

    test1()


# functools.partial
def chapter_9_6():
    """
    9.6. Defining a Decorator That Takes an Optional Argument
        functools.partial()
        You would like to write a single decorator that can be used without arguments, such as @decorator, or with
    optional arguments, such as @decorator(x,y,z). However, there seems to be no straightforward way to do it due
    to differences in calling conventions between simple decorators and decorators taking arguments

    为装饰器参数指定默认值。

    ====================
    @logged(level=logging.CRITICAL, name='example')
    def spam():
        print('Spam!')
    =========>
    def spam():
        print('Spam!')
    spam = logged(level=logging.CRITICAL, name='example')(spam)
    ====================
    """

    def test1():
        from functools import wraps, partial
        import logging

        def logged(func=None, level=logging.DEBUG, name=None, message=None):
            if func is None:
                return partial(logged, level=level, name=name, message=message)
            # 利用partial函数，将传入装饰器中的参数进行初始化后返回同一个装饰器函数，新的装饰器函数将接受被装饰函数作为第一个参数。

            logname = name if name else func.__module__
            log = logging.getLogger(logname)
            logmsg = message if message else func.__name__

            @wraps(func)
            def wrapper(*args, **kwargs):
                log.log(level, logmsg)
                return func(*args, **kwargs)

            return wrapper

        @logged
        def add(x, y):
            return x + y

        @logged(level=logging.CRITICAL, name='example')
        def spam():
            print('Spam!')

    def test2():
        import functools

        def decorator(func=None, *, a=1, b=2, c=3):
            if func is None:
                return functools.partial(decorator, a=a, b=b, c=c)

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print("decorator", a, b, c)
                return func(*args, **kwargs)

            return wrapper

        @decorator
        def f1(a, b):
            return a + b

        @decorator(a=10, c=30)
        def f2(a, b):
            return a + b

    def test3():
        def decorator(a=10, b=20, c=30):
            def inner(func):
                def wrapper(*args, **kwargs):
                    print("decorator", a, b, c)
                    return func(*args, **kwargs)

                return wrapper

            return inner

        @decorator()
        def add(a, b):
            return a + b

        print(add(1, 2))


def chapter_9_7():
    """
    ???
    9.7. Enforcing Type Checking on a Function Using a Decorator
        function signature object
        one aspect of decorators is that they only get applied once, at the time of function definition.

        inspect.signature()方法

    """
    from inspect import signature
    from functools import wraps

    def test1():
        def typeassert(*ty_args, **ty_kwargs):
            def decorate(func):
                if not __debug__:
                    return func
                sig = signature(func)
                bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

                @wraps(func)
                def wrapper(*args, **kwargs):
                    bound_values = sig.bind(*args, **kwargs)
                    for name, value in bound_values.arguments.items():
                        if name in bound_types:
                            if not isinstance(value, bound_types[name]):
                                raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
                    return func(*args, **kwargs)

                return wrapper

            return decorate

    def test2():
        def spam(x, y, z=42):
            pass

        sig = signature(spam)
        print(sig)
        print(sig.parameters['z'].name)
        print(sig.parameters['z'].default)
        print(sig.parameters['z'].kind)

        bound_types = sig.bind_partial(int, z=int)
        print(bound_types)
        print(bound_types.arguments)

        bound_types = sig.bind(1, 2, 3)
        print(bound_types.arguments)


def chapter_9_8():
    """
    9.8. Defining Decorators As Part of a Class
        You want to define a decorator inside a class definition and apply it to other functions or methods.
        In particular, the built-in @property decorator is actually a class with getter(), setter(), and deleter()
    methods that each act as a decorator.
        The key reason why it’s defined in this way is that the various decorator methods are
    manipulating state on the associated property instance. So, if you ever had a problem
    where decorators needed to record or combine information behind the scenes, it’s a
    sensible approach.

    类中定义的装饰器分为类实例装饰器和类装饰器。
    @property本质上就是一个包含getter()/setter()/deleter()方法的类，每一个方法都是一个装饰器。
    在类中定义装饰器主要用于记录和组合应用场景的全局信息。

    """

    def test1():
        from functools import wraps

        class A:
            def decorator_as_instance(self, func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                    print('Decorator as instance')
                    return func(*args, **kwargs)

                return wrapper

            @classmethod
            def decorator_as_classmethod(cls, func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                    print('Decorator as classmethod')
                    return func(*args, **kwargs)

                return wrapper

        a = A()

        @a.decorator_as_instance
        def spam():
            pass

        @A.decorator_as_classmethod
        def grok():
            pass


def chapter_9_9():
    """
    9.9. Defining Decorators As Classes
        You want to wrap functions with a decorator, but the result is going to be a callable instance. You need
    your decorator to work both inside and outside class definitions.
        To define a decorator as an instance, you need to make sure it implements the __call__() and __get__() methods.
        The purpose of __get__() is to create a bound method object (which ultimately supplies the self argument to
    the method). If the method is accessed on a class, the instance argument to __get__() is set to None and the
    Profiled instance itself is just returned.

        将类定义为装饰器，将类的实例作为装饰器，需要实现__call__()/__get__()方法。

        python中创建一个实例的方法有三种方式:
        1. 直接在类中定义方法。
        2. 将一个函数赋值给类的属性。
        3. 通过types.MethodType动态地创建方法。
    """
    import types
    from functools import wraps

    def test1():
        class Profiled:
            def __init__(self, func):
                wraps(func)(self)  # partial()
                self.ncalls = 0

            def __call__(self, *args, **kwargs):
                self.ncalls += 1
                return self.__wrapped__(*args, **kwargs)

            def __get__(self, instance, cls):
                if instance is None:
                    return self
                else:
                    return types.MethodType(self, instance)

        @Profiled
        def add(x, y):
            return x + y

        class Spam:
            @Profiled
            def bar(self, x):
                print(self, x)

        print(add(2, 3))
        print(add(4, 5))
        print(add.ncalls)
        s = Spam()
        s.bar(1)
        s.bar(2)
        s.bar(3)
        s = Spam()

        def grok(self, x):
            pass

        print(grok.__get__(s, Spam))

    def test2():
        def Profiled(func):
            ncalls = 0

            @wraps(func)
            def wrapper(*args, **kwargs):
                nonlocal ncalls
                ncalls += 1
                return func(*args, **kwargs)

            wrapper.ncalls = lambda: ncalls
            return wrapper

        @Profiled
        def add(x, y):
            return x + y

    def test3():
        class C:
            def __call__(self, a, b):
                print(a, b)

        c = C()
        c(1, 2)


def chapter_9_10():
    """
    9.10. Applying Decorators to Class and Static Methods
        You want to apply a decorator to a class or static method.
        Applying decorators to class and static methods is straightforward, but make sure that your decorators are
    applied before @classmethod or @staticmethod.
        If you get the order of decorators wrong, you’ll get an error. The problem here is that @classmethod and
    @staticmethod don’t actually create objects that are directly callable. Instead, they create special descriptor
    objects, as described in Recipe 8.9.
    """
    import time
    from functools import wraps

    def timethis(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            r = func(*args, **kwargs)
            end = time.time()
            print(end - start)
            return r

        return wrapper

    class Spam:
        @timethis
        def instance_method(self, n):
            print(self, n)
            while n > 0:
                n -= 1

        @classmethod
        @timethis
        def class_method(cls, n):
            print(cls, n)
            while n > 0:
                n -= 1

        @staticmethod
        @timethis
        def static_method(n):
            print(n)
            while n > 0:
                n -= 1

    s = Spam()
    s.instance_method(1000000)
    Spam.class_method(1000000)
    Spam.static_method(1000000)


def chapter_9_11():
    """
    9.11. Writing Decorators That Add Arguments to Wrapped Functions
        You want to write a decorator that adds an extra argument to the calling signature of the wrapped function.
    However, the added argument can’t interfere with the existing calling conventions of the function.
        Keyword-only arguments are easy to add to functions that also accept *args and **kwargs parameters.
        One tricky part here concerns a potential name clash between the added argument and the arguments of the
    function being wrapped.
    """
    from functools import wraps
    import inspect

    def optional_debug(func):
        # 处理keyword-only和kwargs参数key值重复的问题
        if 'debug' in inspect.getargspec(func).args:
            raise TypeError('debug argument already defined')

        @wraps(func)
        def wrapper(*args, debug=False, **kwargs):
            if debug:
                print('Calling', func.__name__)
            return func(*args, **kwargs)

        # signature ???
        sig = inspect.signature(func)
        parms = list(sig.parameters.values())
        parms.append(inspect.Parameter('debug', inspect.Parameter.KEYWORD_ONLY, default=False))
        wrapper.__signature__ = sig.replace(parameters=parms)

        return wrapper

    @optional_debug
    def spam(a, b, c):
        print(a, b, c)

    spam(1, 2, 3)
    spam(1, 2, 3, debug=True)


def chapter_9_12():
    """
    9.12. Using Decorators to Patch Class Definitions
        You want to inspect or rewrite portions of a class definition to alter its behavior, but without using
    inheritance or metaclasses.
    """
    pass
