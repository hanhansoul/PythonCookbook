from collections import deque

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(4)
d.appendleft(5)
print(d)
d.pop()
d.popleft()
print(d)

d.extend(['a', 'b', 'c'])
d.extendleft("efg")

d1 = deque(d)
d2 = deque((12, 34, 56))
d3 = deque([1, 2, 3, 4])
d4 = deque({'a': 1, 'b': 5, 'c': 3})  # deque(['b', 'c', 'a'])
