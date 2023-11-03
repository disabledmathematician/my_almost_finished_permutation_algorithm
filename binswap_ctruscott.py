#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:00:41 2023
Getting there. Charles Thomas Wallace Truscott Watters 

127 Broken Head Rd, Suffolk Park NSW 2481

Byron Bay


"""
import math
def Charles():
    L = [1, 2, 3, 4, 5]
    lL = len(L) - 1
    x = 1
    x <<= lL
    y = x
    c = lL
    d = len(L) - 1
    count = 0
    x = 1
    y = 1
#    print("{:05b}".format(x))
#    print("{:05b}".format(y))
    c, b = len(L) - 1, len(L) - 1
    print("{} stays in position {}".format(c, b))
    count = 0
#    print("{:05b}".format(1 << c))
#    print("{:05b}".format(1 << c - 1))
#    p, q = int(1) << c, int(1) << (c - 1)
#    print("{:05b}".format(int(p + q) ^ int('11111', 2)))
    c = len(L) - 2
    b = c - 1
    x <<= c
    y <<= b
    while b >= 0:
    	print("{} is swapped with {}".format(c, b))
    	print("{:05b}".format(x))
    	print("{:05b}".format(y))
    	print("{:05b}".format((x + y) ^ int('11111', 2)))
    	count += math.factorial(3)
    	b -= 1
    	y >>= 1
    while d >= 3:
        c = d - 1
        while c >= 0:
#            print("{:05b}".format(x))
#            print("{:05b}".format(y))
            print("Outer loop: {} is swapped with {}".format(d, c))
            x = 1
            y = 1
            x = x << d
            y = y << c
            print("{:05b}".format(x))
            print("{:05b}".format(y))
            print("{:05b}".format((x + y) ^ (int('11111', 2))))
            count += math.factorial(3)
            c2 = c
            y2 = y
            c2 += 1
      #      while c2 <= ((len(L) - 1)) and c != d - 1:
   #             print("Inner loop: {} is swapped with {}".format(c, c2))
#                count += 6
 #               c2 += 1
            y >>= 1
            c -= 1
        d -= 1
    print(count * 2)
#    print("Count plus one times five: 5! or len(L) or " +  str((count + 1) * 5))
    print("Needs individual mutation for offset")
if __name__ == """__main__""": Charles()