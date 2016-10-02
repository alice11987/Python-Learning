# -*- coding: utf-8 -*-
#quite often we have a list of items of the lines in a file - effectively a finite set of things
#We can write a loop to run the loop once for each of the items in a set using the Python for construct
#definite loops- they execute an exact number of times
#definite loops iterate through the members of a set

for i in [5,4,3,2,1] :
    print i

print 'Blastoff!'

friends = ['Joseph', 'Glenn', 'Sally', 'Alice']

for name in friends :
    print 'Happy New Year!:', name
    
print 'Done!'