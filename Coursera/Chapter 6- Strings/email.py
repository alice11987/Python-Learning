# -*- coding: utf-8 -*-
#from stephen.marquard@uct.ac.za sat jan  5 09:14:16 2008
#这是用来找哪一个字是在哪一个格子

data = 'from stephen.marquard@uct.ac.za sat jan  5 09:14:16 2008'
atpos = data.find('@')
print atpos 
#会拿到21

#这里是要找在@以后的第一个空格
sppos = data.find('',atpos)
print sppos
#会拿到31

#从@（atpos）开始，print到空格（appos），而不包括空格（appos）
#+1是因为从那个的后面一个字开始
host = data[atpos+1 :sppos]
print host
#会拿到 uct.ac.za