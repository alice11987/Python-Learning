# -*- coding: utf-8 -*-
#finishing an iteration with 'continue'
#the continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration

while True :
    line = raw_input('>')
    if line[0] == '#' :
        continue 
    if line == 'done' :
        break 
    print line
print 'Done!'