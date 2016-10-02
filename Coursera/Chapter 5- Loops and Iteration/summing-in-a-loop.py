# -*- coding: utf-8 -*-
#To add up a value we encounter in a loop, 
#we introduce a sum variable that starts at 0 and 
#we add the value to the sum each time through the loop
#这是算［ ］ 里面所有数字的值的总数，而不是数量！
#这里的thing其实就是［ ］里面的号码
#after后面就是所有［ ］里面的数目的总数
#一开始设zork ＝ 0 因为是从0 算起。sum！！！
zork = 0
print 'before', zork
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print zork,'|', thing
print 'After', zork