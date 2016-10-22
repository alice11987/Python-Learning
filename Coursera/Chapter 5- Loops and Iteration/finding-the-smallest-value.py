# -*- coding: utf-8 -*-
#找最小值不能用找最大值的方法来找，因为smallest我们不知道应该放多少
#none是这里的python特别code
#line13 是我自己加上的（为了整齐明确）
#
smallest = None
print 'before:'
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest : 
        smallest = value 
    print 'smallest so far | numbers:'
    print smallest, '|', value

print 'so, the smallest number is:', smallest