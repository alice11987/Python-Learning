# -*- coding: utf-8 -*-
#An average just combines the counting and sum patterns
#and divides when the loop is done
#把之前的算几个loop，和loop值的sum，加在一个程序，计算average
#average ＝ sum（总值） 除于 count（数量）
#
#
#
count = 0
sum = 0
print 'before', count, sum
for value in [9,41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print 'count | sum | value'
    print count,',', sum,',', value
print 'after', count,',', sum,',', float(sum / count) 