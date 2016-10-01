# -*- coding: utf-8 -*-

def max_min_ex(*args):
    print(args)
    return max(args), min(args)

x, y = max_min_ex(5,6,2,3,10,324,232)
print(x)
print(y)