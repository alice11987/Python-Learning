# -*- coding: utf-8 -*-
#this is a simple loop that loops through
#each letter in the strings and counts 
#the number of times the loop encounter
#the 'a' character
#这是用来计算在一个string里面其中一个英文字母的数量
#比如说这里算的是a

word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print count 