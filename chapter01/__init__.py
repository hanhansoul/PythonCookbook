from collections import deque
import heapq

q = deque(maxlen=5)
p = deque()

for i in range(20):
    p.append(i)

print(p)

while len(p):
    print(p.pop())

# heapq

import heapq
import random

nums = [1, 5, 3, 6, 3, 3, 1, 344, 12, 31, 35, 25, 3]
heap = list(nums)
heapq.heapify(heap)

heap = []
for i in range(20):
    heapq.heappush(heap, random.randint(1, 100))

print(heapq.nlargest(5, heap))

while len(heap):
    print(heapq.heappop(heap))

from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
