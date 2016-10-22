# -*- coding: utf-8 -*-
#If we just want to search and know if a value was found
#we use a variable that starts at False and is set to True
#as soon as we find what we are looking for
#如果一找到有3，从3下面起的会显示已找到，也就是这里的true
#要是我们不要那么麻烦，显示那么多号码，可以直接把line13去掉，这样就会直接显示true，
#但只单单能表明，list里面有3这个数字
found = False
print 'before', found
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3 :
        found = True
        break
        #这里的break是我自己加上去的，因为找到了3，我们没有必要再让程序继续找下去
        #direct显示在这里找到了就可以了
    print found, value

print 'after', found
