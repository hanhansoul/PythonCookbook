"""
heapq 最大堆/最小堆

heapq.heappush(heap, item)
添加元素

heapq.heappop(heap)
删除元素

heapq.heappushpop(heap, item)
添加一个元素，然后从堆中取出最小的一个元素。

heapq.heapreplace(heap, item)
先取出堆中最小的一个元素，然后添加新的元素。

heapq.heapify(x)
在O(n)时间复杂度内将list转换为一个heap。

heapq.merge(*iterables, key=None, reverse=False)
将多个有序的可迭代对象合并为一个有序对象，返回该对象的迭代器。
类似于sorted(itertools.chain(*iterable))

heapq.nlargest(n, iterable, key=None)
从iterable中返回前n个最大的元素。

heapq.nsmallest(n, iterable, key=None)
从iterable中返回前n个最小的元素。

"""
import heapq


# 堆排序
# 不是稳定排序，sorted()是稳定排序
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


heapsort([1, 3, 5, 7, 3, 5, 2, 6, 3, 0, 8, 3, ])

l1 = [4, 5, 7, 8, 9]
l2 = [1, 3, 5, 7, 9]
l3 = [6, 9, 10, 13, 25]
c1 = heapq.merge(l1, l2, l3)
for item in c1:
    print(item)

l4 = [6, 2, 8, 4, 9, 1, 6, 2]
l5 = [6, 7, 3, 4, 1, 2, 4]
heapq.heapify(l4)
heapq.heapify(l5)
# c2 = heapq.merge(heapq.heapify(l4), heapq.heapify(l5))
c2 = heapq.merge(l4, l5)
for item in c2:
    print(item)

