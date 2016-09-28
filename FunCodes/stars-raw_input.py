# -*- coding:utf-8 -*-
 
import sys
def draw_pic():
    size = int(input("Please set your size ´・ω・`:"))
    for i in range(1, 2*size):
        num = abs(size-i)
        print(" "*num+"★ "*(size-num))
        
if __name__ == "__main__":
    draw_pic()