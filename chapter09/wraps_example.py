def test1():
    def partial(func, *args, **kwargs):
        def newfunc(*fargs, **fkwargs):
            print(fkwargs)
            print(fargs)
            newkeywords = kwargs.copy()
            newkeywords.update(fkwargs)
            return func(*args, *fargs, **newkeywords)

        newfunc.func = func
        newfunc.args = args
        newfunc.kwargs = kwargs
        return newfunc

    def add(x, y):
        return x + y

    add2 = partial(add, y=2)
    add2(3)
    add2(x=3)
    print(add2.kwargs)


# update_wrapper
def test2():
    def wrapper(f):
        def wrapper_function(*args, **kwargs):
            """这个是修饰函数"""
            return f(*args, **kwargs)

        return wrapper_function

    @wrapper
    def wrapped():
        """这个是被修饰的函数"""
        print("wrapped")

    def func(x, y):
        return x + y

    res = wrapper(func)(2, 3)
    print(res)

    print(wrapped.__doc__)
    print(wrapped.__name__)


def test3():
    from functools import update_wrapper

    def new_wrapper(f):
        def wrapper_function(*args, **kwargs):
            """这个是修饰函数"""
            return f(*args, **kwargs)

        update_wrapper(wrapper_function, f)
        return wrapper_function

    @new_wrapper
    def new_wrapped():
        """这个是被修饰的函数"""
        print("new_wrapped")

    print(new_wrapped.__doc__)
    print(new_wrapped.__name__)


#  wraps实现
def test4():
    from functools import partial
    from functools import update_wrapper
    WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
                           '__annotations__')
    WRAPPER_UPDATES = ('__dict__',)

    def wraps(wrapped,
              assigned=WRAPPER_ASSIGNMENTS,
              updated=WRAPPER_UPDATES):
        return partial(update_wrapper, wrapped=wrapped,
                       assigned=assigned, updated=updated)


def test5():
    from functools import wraps

    def wrapper(f):
        @wraps(f)
        def wrapper_function(*args, **kwargs):
            """这个是修饰函数"""
            return f(*args, **kwargs)

        return wrapper_function

    @wrapper
    def wrapped():
        """这个是被修饰的函数
        """
        print('wrapped')


def test6():
    """
    返回的是一个闭包，其中的属性值都被保存起来了。
    """

    def decorator(*dargs, **dkargs):
        def wrapper(func):
            def _wrapper(*args, **kargs):
                print("decorator param:", dargs, dkargs)
                print("function param:", args, kargs)
                return func(*args, **kargs)

            return _wrapper

        return wrapper

    @decorator(1, a=2)
    def foo(x, y=0):
        print("foo", x, y)

    foo(3, 4)

    def spam(x, y):
        print(x, y)

    decorator(1, a=2)(spam)(3, 4)


def test7():
    def d1(func):
        print("d1")

        def inner():
            print("inner1")
            func()
            print("inner1")

    @d1
    def f1():
        print("f1")


def test():
    def wrapper(f):
        def wrapper_function(*args, **kwargs):
            print("decorator")
            return f(*args, **kwargs)

        return wrapper_function

    @wrapper
    def wrapped():
        print("wrapped")

    def func(x, y):
        return x + y

    f = func

    wrapped
    wrapper(wrapped)

    wrapper(func)(1, 2)

    g = wrapped
