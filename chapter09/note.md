## chapter 9.4 (*)
为装饰器提供参数。

有两种方式为装饰器提供参数：

- 添加额外一层函数接受参数；

- 使用functools.partial()函数。

## chapter 9.5 (*)

在使用装饰器时，可以通过装饰器为被装饰函数绑定参数。在某些情况下，用户需要在程序运行过程中动态地修改被装饰函数绑定的参数值。

此时可以通过其他装饰器，利用setattr函数为被装饰函数绑定相关参数的setter方法实现该目标。

## chapter 9.6 (*)

使用functools.partial()函数为装饰器提供默认参数。

## chapter 9.7

使用装饰器实现函数参数的类型检查。

## chapter 9.8 (*)

将类中的方法作为装饰器，包括实例方法装饰器和类方法装饰器。

## chapter 9.9 (*)

将类作为装饰器，需要实现类的__call__()和__get__()方法

## chapter 9.10 (*)

注意自定义装饰器的位置要放在@classmethod / @staticmethod之后，@classmethod / @staticmethod应在最外层。

## chapter 9.11

利用装饰器为函数参数列表添加新参数。

## chapter 9.12 (*)

利用装饰器为函数添加新属性或方法。

## chapter 9.13 (***)

利用metaclass控制实例创建过程，实现单例模式，缓存或其他模式。

## chapter 9.14

metaclass获取类属性定义的顺序。

## chapter 9.21 (*)

避免重复的property方法。

- 创建一个property工厂方法，用于统一定义property并返回。

- functools.partial()函数

## chapter 9.22 (*)

@contextmanager定义with语句，重写__enter__()和__exit__()方法。