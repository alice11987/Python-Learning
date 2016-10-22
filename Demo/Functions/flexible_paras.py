# -*- coding: utf-8 -*-
#flexible parameter＝可变参数，在第5行的那里是重点，max 和min。
def max_min_ex(*args):
    print(args)
    return max(args), min(args)

x, y = max_min_ex(5,6,2,3,10,324,232)
print(x)
print(y)