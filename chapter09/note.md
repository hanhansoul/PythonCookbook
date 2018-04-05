### bound method 和 unbound method

bound method比unbound method多了一个实例绑定的过程。a.f是bound method，A.f是unbound method。

类通过__get__()方法获取方法属性：

- 当通过类来获取方法属性的时候，得到的是非绑定方法对象。
- 当通过实例来获取方法属性的时候，得到的是绑定方法对象。

### 定义带参数的装饰器

方法1：

    def decorator(a, b, c)：
        def inner(func):
            def wrapper(*args, **kwargs):
                print("decorator", a, b, c)
                return func(*args, **kwargs)
                
    @decorator(1, 2, 3)
    def f(a, b):
        return a + b
        
方法2：使用functools.partial()方法为装饰器绑定参数，该方法与之后未装饰器参数指定默认值的方法相同。

    def decorator(func=None, *, a, b, c):
        if func is None:
            return functools.partial(decorator, a=a, b=b, c=c)
        else:
            def wrapper(*args, **kwargs):
                print("decorator", a, b, c)
                return ff(*args, **kwargs)
            return wrapper

### 为装饰器参数添加默认值

可利用functools.partial()方法为装饰器参数提供默认值。

装饰器的工作原理：

    @decorator
    def f(a, b):
        return a + b
    # --------------------
    # 等同于:
    # --------------------
    def f(a, b):
        return a + b
    f = decorator(f)

带参数的装饰器的工作原理：
    
    @decorator(1, 2, 3)
    def f(a, b):
        return a + b
    # --------------------
    # 等同于:
    # --------------------
    def f(a, b):
        return a + b
    f = decorator(1, 2, 3)(f)

    import functools
    from functools import wraps

为装饰器参数指定默认值：

    import functools
    def decorator(func=None, *, a=1, b=2, c=3):
        if func is None:
            # functools.partial()在有自定义参数时为decorator参数赋值。
            # 若未提供参数，则func不为None，不调用partial()方法。
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
        
另一种为装饰器指定默认参数的方式：

    import functools
    def decorator(a=1, b=2, c=3):
        def inner(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print("decorator", a, b, c)
                return func(*args, **kwargs)
            return wrapper
        return inner
        
    # 此处的()不能省略
    @decorator()
    def f1(a, b)
        return a + b
    # --------------------
    # wrong!
    # @decorator
    # def f2(a, b)
    #     return a + b

## 类与装饰器

### 在类中定义装饰器

类的实例方法或类方法都可以被定义为装饰器。类的实例方法的第一个参数为self；而类方法由@classmethod
修饰，方法的第一个参数为cls，即类本身。

方法中的self或cls参数通常不会发挥作用，只有在装饰器中需要访问附加在实例或类的状态属性的时候，才需要
通过self或cls访问。

    from functools import wraps

    class A:
        # 实例方法
        def decorator_as_instance(self, func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                print('Decorator as instance')
                return func(*args, **kwargs)

            return wrapper
        # 类方法
        @classmethod
        def decorator_as_classmethod(cls, func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                print('Decorator as classmethod')
                return func(*args, **kwargs)

            return wrapper

    # 实例方法装饰器。
    # 首先需要一个实例对象，其他与一般装饰器类似。
    a = A()
    @a.decorator_as_instance
    def spam():
        pass

    # 类方法装饰器
    # 不需要实例，直接通过类调用。
    @A.decorator_as_classmethod
    def grok():
        pass

### 类装饰器

除了类的成员方法可以被定义为装饰器之外，类本身也可以被定义为装饰器。

为定义一个类装饰器，必须实现__call__()和__get__()方法。

其中，实现__get__()方法的目的是为了创建一个绑定的方法对象。实现__get__()
使得类装饰器实现了descriptor接口，这一特性在类装饰器修饰其他类的成员方法时
十分重要，被类装饰器修饰的成员方法变成了类的一个descriptor。

types.MethodType()

    import types
    from functools import wraps
    # 类装饰器
    # 用于统计被装饰方法被调用的次数
    class Profiled:
        def __init__(self, func):
            wraps(func)(self)
            self.ncalls = 0

        def __call__(self, *args, **kwargs):
            self.ncalls += 1
            return self.__wrapped__(*args, **kwargs)

        def __get__(self, instance, cls):
            if instance is None:
                return self
            else:
                return types.MethodType(self, instance)
    # --------------------
    # 装饰函数时，与其他装饰器没有区别，并没有使用__get__()方法
    @Profiled
    def add(x, y):
        return x + y
    # 等同于：
    def add(x, y):
        return x + y
    add = Profiled(add)
    # --------------------
    # 装饰类实例方法，需要使用类装饰器中定义的__get__()方法
    class Spam:
        @Profiled
        def bar(self, x):
            print(self, x)
    # 等同于
    class Spam:
        def bar(self, x):
            print(self, x)
            
        bar = Profiled(bar)
    # 可见此时bar成为了一个类成员变量，是一个non-data descriptor。
    s = Spam()
    s.bar(1)    # type(s).__dict__['bar'].__get__(s, type(s))
    

## 使用装饰器装饰类方法或静态方法

与其他类型装饰器使用方法一样，但需要保证装饰器出现在@classmethod或@staticmethod之前。

## 装饰器应用

### 方法参数的类型安全

