# -*- coding: utf-8 -*-

def max_min(a, b, c):
    arr = (a, b, c)
    return max(arr), min(arr)

x, y = max_min(1)
print(x)
print(y)
print(max_min(5, 2, 8))