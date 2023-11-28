from functools import cmp_to_key
from math import prod


def cmp(l, r):
    match l, r:
        case int(), int(): return (l > r) - (l < r)
        case int(), list(): return cmp([l], r)
        case list(), int(): return cmp(l, [r])
        case list(), list():
            for z in map(cmp, l, r):
                if z:
                    return z
            return cmp(len(l), len(r))


packets = [[*map(eval, x.split())]
           for x in open('day13/13input.txt').read().split('\n\n')]
print(sum(i for i, p in enumerate(packets, 1) if cmp(*p) == -1))
