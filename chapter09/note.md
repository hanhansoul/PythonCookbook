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

类的实例方法或类方法都可以被定义为装饰器。


## 装饰器应用

### 方法参数的类型安全

