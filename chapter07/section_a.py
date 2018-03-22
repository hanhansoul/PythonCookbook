def chapter_7_1():
    """
    7.1. Writing Functions That Accept Any Number of Arguments

    变长的函数参数列表
    *args 以tuple参数形式传入
    **kwargs 以dict参数形式传入

    func(positional-arg, *-arg, keyword-only-arg, **-arg)
    func(positional-only-arg, [positional-or-keyword-arg], keyword-only-arg)

    函数中，*运算符将[]或()拆分为positional-arg，**运算符将{}拆分为keyword-arg。
    ll = [1, 2, 3, 4]
    tt = (10, 20, 30, 40)
    dd = {'a': 1, 'b': 2, 'c': 3}
    test1(*ll, *tt, **dd) => test1(1, 2, 3, 4, 10, 20, 30, 40, a=1, b=2, c=3)

    positional-arg必须在keyword-arg之前提供
    *args只能放在最后一个positional-arg之后，作为最后的positional-arg
    **kwargs只能放在所有参数之后
    """

    def test1(*args, **kwargs):
        print(args)  # tuple
        print(kwargs)  # dict

    def test2(first, *rest, **rest_rest):
        print(first)
        print(rest)
        print(rest_rest)

    def test3(x, *args, y):
        print(x)
        print(args)
        print(y)

    def test4(x, *args, y, **kwargs):
        print(x)
        print(args)
        print(y)
        print(kwargs)

    def test5(x, y, z, *args, a, b, **kwargs):
        pass

    test2(1, 2, 3, 4, a=1, b=2, c=4)
    test3(1, y=2)
    test4(1, 2, 3, 4, y=3, a=1, b=2)

    ll = [1, 2, 3, 4]
    tt = (10, 20, 30, 40)
    dd = {'a': 1, 'b': 2, 'c': 3}
    test1(*ll, *tt, **dd)

    # test5(1, 2, z=3, *tt, a=10, b=20)  # wrong
    test5(1, 2, 3, *tt, a=10, b=20)


def chapter_7_2():
    """
    7.2. Writing Functions That Only Accept Keyword Arguments
    A function only accepts certain arguments by keyword.

    此处*与*arg类似，但不接受任何参数，只作为positional-arg和keyword-arg的分隔点
    """

    def recv(maxsize, *, block):
        print(maxsize)
        print(block)

    def test2(*values, clip=None):
        m = min(values)
        if clip is not None:
            m = clip if clip > m else m
        return m

    # recv(1024, True) # error
    recv(1024, block=True)
    test2(1, 5, 2, -5, 10)
    test2(1, 5, 2, -5, 10, clip=0)


def chapter_7_3():
    """
    7.3. Attaching Informational Metadata to Function Arguments
    annotation

    :与->可以提供的参数类型只能作为参考，并不具有强制性。
    __annotations__ 保存了类型信息
    """

    def add(x: int, y: int) -> int:
        return x + y

    print(add.__annotations__)
    print(add('a', 'b'))
    print('a' + 'b')


def chapter_7_4():
    """
    7.4. Returning Multiple Values from a Function
    Return multiple values from a function

    通过返回一个tuple使函数可以返回多个值。
    a, b, c ==> (a, b, c)
    """

    def test1():
        return 1, 2, 3

    a, b, c = test1()
    print(a, b, c, sep='\n')


def chapter_7_5():
    """
    7.5. Defining Functions with Default Arguments
        The values assigned as a default are bound only once at the time of function definition.
        The values assigned as defaults should always be immutable objects, such as None, True, False, numbers,
    or strings.	Specifically, never write code like this:

        def spam(a, b=[]):	# NO!
            pass

        def spam(a, b=None):
            if not b: 		# Use 'b is None' instead
                b = []

        函数参数的默认值只会在函数定义的时候绑定一次。
        x = 42
        def spam(a, b=x):
            pass
        spam(1) # b=42
        x = 21
        spam(1) # b=42

        函数参数的默认值应该绑定不可变对象，而不能是列表或字典变量。
        当该参数被函数返回并被修改时，该函数参数的默认值也会被修改。

        逻辑运算中零长度string，空list，空tuple，空dict都为False
    """
    x = 42

    def spam(a, b=x):
        print(a, b)

    spam(1)
    x = 30
    spam(1)

    def spam(a, b=[]):
        print(b)
        return b

    x = spam(1)
    print(x)
    x.append(99)
    x.append('ABC')
    print(x)
    spam(1)


def chapter_7_6():
    """
    7.6. Defining Anonymous or Inline Functions
        lambda
        You need to supply a short callback function for use with an operation such as sort(), but you don’t
    want to write a separate one-line function using the def statement. Instead, you’d like a shortcut that
    allows you to specify the function “in line.”
        no other language features, including multiple statements, conditionals, iteration, and exception handling, can be included.
    """
    print((lambda x, y: x + y)(1, 2))
    names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
    ordered_names = sorted(names, key=lambda name: name.split()[-1].lower())
    print(ordered_names)


def chapter_7_7():
    """
    7.7. Capturing Variables in Anonymous Functions

    lambda中的变量是动态绑定的。
    但可以通过为lambda中的变量提供默认值的方式进行变量绑定。
    """
    x = 10
    a = lambda y: x + y
    print(a(10))
    x = 20
    b = lambda y: x + y
    print(a(10))
    print(b(10))
    # If you want an anonymous function to capture a value at the point of definition and keep it
    x = 10
    a = lambda y, x=x: x + y
    x = 20
    b = lambda y, x=x: x + y
    print(a(10))
    print(b(10))
    #
    funcs = [lambda x, n=n: x + n for n in range(5)]
    for f in funcs:
        print(f(0))


def chapter_7_8():
    """
    7.8. Making an N-Argument Callable Work As a Callable with Fewer Arguments
        functools.partial()
        The partial() function allows you to assign fixed values to one or more of the arguments, thus
    reducing the number of arguments that need to be supplied to subsequent calls.
    偏函数
    """
    import functools
    import math

    def test1():
        def spam(a, b, c, d):
            print(a, b, c, d)

        s1 = functools.partial(spam, 1)  # a = 1
        s1(2, 3, 4)
        s1(4, 5, 6)
        s2 = functools.partial(spam, d=42)  # d = 42
        s2(1, 2, 3)
        s2(3, 4, 5)
        s3 = functools.partial(spam, 1, 2, d=42)  # a = 1, b = 2, d = 42
        s3(10)
        s3(20)

    def test2():
        points = [(1, 2), (3, 4), (5, 6), (7, 8)]

        def distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return math.hypot(x2 - x1, y2 - y1)

        pt = (4, 3)
        points.sort(key=functools.partial(distance, pt))

    def chapter_7_9():
        """
        7.9. Replacing Single Method Classes with Functions
            Single-method classes can be turned into functions using closures.
            The only reason you might have a single-method class is to store additional state for use in the method. A
        closure is just a function, but with an extra environment of the variables that are used inside the function. A key
        feature of a closure is that it remembers the environment in which it was defined.
            the problem of attaching additional state to a function
        """
        pass

    """
    A callback function is a function which is:
        1. passed as an argument to another function, and,
        2. is invoked after some kind of event.
    Once its parent function completes, the function passed as an argument is then called.
    """

    def chapter_7_10():
        """
        ???
        7.10. Carrying Extra State with Callback Functions
            You’re writing code that relies on the use of callback functions (e.g., event handlers, completion callbacks,
        etc.), but you want to have the callback function carry extra state for use inside the callback function.
            This recipe pertains to the use of callback functions that are found in many libraries and frameworks—especially
        those related to asynchronous processing.
            One way to carry extra information in a callback is to use a bound-method instead of a simple function.
            1. instance
            2. closure
            3. coroutine
            4. partial

        当回调函数需要与其他的全局变量交互式，可以用一个类封装该回调函数与相关全局变量，再将该回调函数传递给对应函数。
        """

        def print_result(result):
            print(result)

        def add(x, y):
            return x + y

        def apply_async(func, args, *, callback):
            result = func(*args)
            callback(result)

        apply_async(add, (2, 3), callback=print_result)

        # class
        class ResultHandler:
            def __init__(self):
                self.sequence = 0

            def handler(self, result):
                self.sequence += 1
                print('[{}] Got: {}'.format(self.sequence, result))

        r = ResultHandler()
        apply_async(add, (2, 3), callback=r.handler)

        # closure
        def make_handler():
            sequence = 0

            def handler(result):
                nonlocal sequence
                sequence += 1

            return handler

        handler = make_handler()
        apply_async(add, (2, 3), callback=handler)

        # partial function
        class SequenceNo:
            def __init__(self):
                self.sequence = 0

        def handler(result, seq):
            seq.sequnce += 1
            print('[{}] Got: {}'.format(seq.sequence, result))

        seq = SequenceNo()
        from functools import partial
        apply_async(add, (2, 3), callback=partial(handler, seq=seq))

        def make_handler_coroutine():
            sequence = 0
            while True:
                result = yield
                sequence += 1
                print('[{}] Got: {}'.format(sequence, result))

        handler = make_handler_coroutine()
        next(handler)
        apply_async(add, (2, 3), callback=handler.send)




def chapter_7_11():
    """
    !!!
    7.11. Inlining Callback Functions
        You’re writing code that uses callback functions, but you’re concerned about the proliferation of small
    functions and mind boggling control flow. You would like some way to make the code look more like a
    normal sequence of procedural steps.
        Callback functions can be inlined into a function using generators and coroutines.
    """
    from queue import Queue
    from functools import wraps

    def apply_async(func, args, *, callback):
        result = func(*args)
        callback(result)

    class Async:
        def __init__(self, func, args):
            self.func = func
            self.args = args

    def inlined_async(func):
        @wraps(func)
        def wrapper(*args):
            f = func(*args)
            result_queue = Queue()
            result_queue.put(None)
            while True:
                result = result_queue.get()
                try:
                    a = f.send(result)
                    apply_async(a.func, a.args, callback=result_queue.put)
                except StopIteration:
                    break

        return wrapper

    def add(x, y):
        return x + y

    @inlined_async
    def test():
        r = yield Async(add, (2, 3))
        print(r)
        r = yield Async(add, ('abc', 'def'))
        print(r)
        r = yield Async(add, (1, 2))
        print(r)

    test()


def chapter_7_12():
    """
    ???
    7.12. Accessing Variables Defined Inside a Closure
        The inner variables of a closure are completely hidden to the outside world. However, you can provide access
    by writing accessor functions and attaching them to the closure as function attributes.
    """

    def sample():
        """
            First, nonlocal declarations make it possible to write functions that change inner variables.
        Second, function attributes allow the accessor methods to be attached to the closure function in a
        straightforward manner where they work a lot like instance methods.
        """
        n = 0

        # Closure function
        def func():
            print('n =', n)

        # Accessor methods for n
        def get_n():
            return n

        def set_n(value):
            nonlocal n  # nonlocal使得函数可以更改内部变量值
            n = value

        # Attach as function attributes
        func.get_n = get_n
        func.set_n = set_n
        return func

    f = sample()
    f()
    f.set_n(10)
    f()
    f()
    f()


def repeat():
    n = 0
    while True:
        n = yield n


# print('n =', n)

# r = repeat()
# print(next(r))
# r.send(10)
# print(next(r))

import sys


def test2():
    class ClosureInstance:
        def __init__(self, locals=None):
            if locals is None:
                locals = sys._getframe(1).f_locals
            self.__dict__.update((key, value) for key, value in locals.items()
                                 if callable(value))

        def __len__(self):
            return self.__dict__['__len__']()

    def Stack():
        items = []

        def push(item):
            items.append(item)

        def pop():
            return items.pop()

        def __len__():
            return len(items)

        return ClosureInstance()
