# -*- coding: utf-8 -*-

def test(a, b, c, d):
    a += 1
    b = 'Alice'
    c.append(2)
    d['age'] = 16
    
    
q = 5
w = 'hello'
e = []
r = {}
test(q, w, e, r)
print(q)
print(w)
print(e)
print(r)
s = r
s['age'] = 17
print(s)
print(r)
d = w
d = 'Alice'
print(w)
print(d)
h = q 
h = 6
print(h)
print(q)