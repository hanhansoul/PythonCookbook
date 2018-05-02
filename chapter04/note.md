## chapter 4.1

使用next()函数遍历迭代器，将StopIteration异常用于标识迭代终止，或标记None作为终止标识。

## chapter 4.2

代理迭代模式。

将一个包含list，tuple或其他可迭代对象的类作为一个自定义的迭代器。实现类的__iter__()方法，__iter__()方法返回当前对象的一个迭代器，
iter(s)即调用的s.\_\_iter__()。

- next()调用__next__()，next(可迭代对象的迭代器)
- iter()调用__iter__()，iter(可迭代对象)
- len()调用__len__()

**可迭代类(collections.abc.Iterable)**

提供了__iter__()或__getitem__()方法。

\_\_iter__()返回一个迭代器对象，实现了\_\_iter__()方法的对象可以用for-in语句进行处理。

**迭代器类(collections.abc.Iterator)**

提供了__iter__()和__next__()方法。

由于Iterator同样是提供了__iter__()方法，迭代器类同样可以用for-in语句处理。

**可迭代对象**

字符串，list，tuple等对象，实现了__iter__()或__getitem__()方法。

**迭代器对象**

可以将可迭代对象视作一个容器，如果需要将容器中的元素依次取出，就需要一个迭代器对象。

通过iter(可迭代对象)即可返回一个迭代器对象。

## chapter 4.3

利用生成器创建新的迭代模式。

## chapter 4.4

Iterator Protocol要求实现__iter__()和__next__()方法。

但这种迭代器实现方法往往十分混乱，推荐使用生成器方式实现迭代功能。

## chapter 4.5

__reversed__()方法实现反向迭代功能。

## chapter 4.6

自定义生成器，使用类将生成器与额外状态信息进行封装。

## chapter 4.7

itertools.islice() 截取迭代器的一个切片。

## chapter 4.8

itertools.dropwhile() 跳过部分可迭代对象。

## chapter 4.9

itertools.permutations() / itertools.combinations() 排列组合。

## chapter 4.10

enumerate() 返回迭代元素的索引值。

## chapter 4.11

zip() / itertools.zip_longest() 并联多个可迭代对象进行迭代。

## chapter 4.12

itertools.chain() 串联多个可迭代对象。

## chapter 4.13

管道

## chapter 4.14

利用递归生成器函数扁平化一个序列。

## chapter 4.15

heapq.merge() 合并多个有序序列为一个有序序列。