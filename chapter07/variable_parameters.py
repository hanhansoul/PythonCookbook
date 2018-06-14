l1 = (1, 2, 3)
l2 = [1, 2, 3]
l3 = range(3)


def func(*args, **kwargs):
    print(args)
    print(*args)
