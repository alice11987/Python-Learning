# -*- coding: utf-8 -*-
#-we can also look at any continuous section 
#of a string using a colon operator
#-the second number is one beyond the 
#end of the slice, "up to but not including"
#-if the second number is beyond the end of the string,
#it stops at the end
#［ ］里面的数目，第一个有包括，第二个没有。
#比方说这里的m＝0 o＝1 n＝2 t＝3 y＝4... 
#所以这里要[0:4]的话呢，就是第0个显示到第3个
#也就是 m o n t 啦
#如果写超过strings的range，系统直接显示到最后一个

s = 'monty python'
print s[0:4]

print s[6:7]

print s[6:20]

#如果只写后面，它就自动从一开始到后面
print s[:2]

#如果只写前面，它就会自动从指定到号码到最后面
print s[8:]

#如果啥也没写，它就会全显示
print s[:]