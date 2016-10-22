# -*- coding: utf-8 -*-
#using a while statement and an iteration variable,
#and the len function, we can construct a loop
#to look at each of the letters in a string individually
fruit = 'banana'
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print index, letter
    index = index + 1

print'---------------------'

#a definite loop using for a statement is much more elegant
#the iteration variable is completely taken care of by the for loop
fruit = 'banana'
for letter in fruit :
    print letter
