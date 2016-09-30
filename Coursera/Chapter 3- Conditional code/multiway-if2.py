x = raw_input('What number do you like?')
x = int(x)
if x < 2 :
    print x, '=you like a small number'
elif x < 10 :
    print x, '=you like a medium number'
elif x < 20 :
    print x, '=you like a bignumber'
elif x < 40 :
    print x, '=you like a large number'
elif x < 100 :
    print x, '=you like a huge number'
else : 
    print x, '=you like a ginormous number'