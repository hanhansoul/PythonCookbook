如果*expr出现在函数参数列表中，expr

## *expr:iterable unpacking operator

## **expr:dictionary unpacking operator

- 函数调用
- 列表推导(list compression)
- 生成器表达式(generator expression)

函数的实参支持任意数量的unpacking操作而不仅仅只是一次unpacking。

    print(*[1], 2, *[3], 4)

    dict(**{'x': 1}, y=2, **{z': 3})

当你需要unpack多个可迭代对象

---

# 函数可变参数列表

对于函数可变参数列表的讨论，需要从函数形参与函数实参两个方面讨论。

## *表达式与**表达式

*表达式用于将任何可迭代对象进行拆包，包括tuple、list、string、file、迭代器与生成器

*range(4),

*表达式用于将tuple、list、string、file、迭代器与生成器等可迭代对象拆包作为函数的可变positional参数。

def func(*args):
    pass

func(*(1, 2, 3))

func(*[4, 5, 6])

**表达式仅用于将字典类型对象拆包作为函数的可变keyword参数。

def func(**kwargs):
    pass

func(a=1)

func(**dict(a=1,b=2,c=3))

## 函数形参

### 变长函数参数

函数参数列表中参数的类型

- positional参数
- 变长的positional参数*args
- keyword参数
- 变长的keyword参数**kwargs

函数参数列表的不同类型参数出现顺序

*args接受任意数量的positional-arg。


## 函数实参

**表达式用于将字典类型对象进行拆包。

print(*[1], 2, *[3, 4])

dict(**{'x': 1}, y=2, **{'z': 3})