# -*- coding: utf-8 -*-
#To count how many times we execute a loop we introduce a counter variable that starts at 0
#and we add one to it each time through the loop
#为了计算有多少个loop，所以前面加上号码
#号码必须＋1，因为程序里第一个数字是0！！！
#下面after是总结。

zork = 0
print 'before', zork
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print zork,')', thing
print 'after', zork
print 'total loops:', zork

