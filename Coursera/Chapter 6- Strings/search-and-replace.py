# -*- coding: utf-8 -*-
#the replace()function is like a 
#"search and replace"operation in a word processor

#it replaces all occurences of search string 
#with the replacement string

#先找出要找出的字，比如这里的o，然后再用要replace的值
#来replace那些o。
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print nstr

greet = 'Hello Bob'
nstr = greet.replace('o', 'X')
print nstr