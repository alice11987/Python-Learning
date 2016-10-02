largest_so_far = -1
print 'before:', largest_so_far
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far :
        largest_so_far = the_num
    print 'new largest | numbers:'
    print largest_so_far, '|', the_num

print 'so, the largest number is:', largest_so_far

# -*- coding: utf-8 -*-
#We make a variable that contains the largest value we have seen so far.
#If the current number we are looking at is larger,
#it is the new largest value we have seen so far.
