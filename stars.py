# -*- coding:utf-8 -*-

import sys
def draw_pic(): 
	line = 3
	for i in range(1, 2*line):
		num = abs(line-i)
		print(" "*num+"* "*(line-num))

if __name__ == "__main__":
	draw_pic()