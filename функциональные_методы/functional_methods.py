def example_filter(x):
    if x % 2 == 0:
        return True
    else:
        return False


li = [1, 2, 3, 4, 5, 6, 7, 8]

f = [i for i in filter(example_filter, li)]

print(f)


def example_map(x):
    return x + 3


li = [1, 2, 3]
m = list(map(example_map, li))
print(m)

from functools import reduce


def example_reduce(x, y):
    return x + y


li = [1, 2, 3, 5]
r = reduce(example_reduce, li)
print(r)


