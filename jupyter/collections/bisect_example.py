import bisect

"""
二分查找
"""

"""
bisect.bisect_left(a, x, lo, hi)
bisect.bisect_right(a, x, lo, hi)
bisect.bisect(a, x, lo, hi)

bisect.insort_left()
bisect.insort_right()
bisect.insort()
"""

ll = [1, 3, 1, 23, 23, 53, 42, 3, 1, 32, 5, 43, 5, 65, 576, 57, 6, 44, 34, 35]
ll = sorted(ll)

i = bisect.bisect_left(ll, 10)
i = bisect.bisect_right(ll, 23)

bisect.insort_left(ll, 10)
