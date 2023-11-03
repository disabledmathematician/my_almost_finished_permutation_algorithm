#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:00:41 2023
Getting there. Charles Thomas Wallace Truscott Watters 

127 Broken Head Rd, Suffolk Park NSW 2481

Byron Bay

In [25]: runfile('/home/charles/Desktop/binswap_ctruscott.py', wdir='/home/charles/Desktop')
4 is swapped with 4
[1, 2, 3, 4, 5]
4 is swapped with 3
[1, 2, 3, 5, 4]
[1, 2, 3, 5, 4]
Previous 3 is swapped to position 4
4 is swapped with 2
[1, 2, 4, 5, 3]
[1, 2, 4, 5, 3]
Previous 2 is swapped to position 3
[1, 2, 5, 4, 3]
Previous 3 is swapped to position 4
4 is swapped with 1
[1, 3, 5, 4, 2]
[1, 3, 5, 4, 2]
Previous 1 is swapped to position 2
[1, 5, 3, 4, 2]
Previous 2 is swapped to position 3
[1, 4, 3, 5, 2]
Previous 3 is swapped to position 4
4 is swapped with 0
[2, 4, 3, 5, 1]
[2, 4, 3, 5, 1]
Previous 0 is swapped to position 1
[4, 2, 3, 5, 1]
Previous 1 is swapped to position 2
[3, 2, 4, 5, 1]
Previous 2 is swapped to position 3
[5, 2, 4, 3, 1]
Previous 3 is swapped to position 4
3 is swapped with 3
[5, 2, 4, 3, 1]
[5, 2, 4, 3, 1]
Previous 3 is swapped to position 4
3 is swapped with 2
[5, 2, 3, 4, 1]
[5, 2, 3, 4, 1]
Previous 2 is swapped to position 3
[5, 2, 4, 3, 1]
Previous 3 is swapped to position 4
3 is swapped with 1
[5, 3, 4, 2, 1]
[5, 3, 4, 2, 1]
Previous 1 is swapped to position 2
[5, 4, 3, 2, 1]
Previous 2 is swapped to position 3
[5, 2, 3, 4, 1]
Previous 3 is swapped to position 4
3 is swapped with 0
[4, 2, 3, 5, 1]
[4, 2, 3, 5, 1]
Previous 0 is swapped to position 1
[2, 4, 3, 5, 1]
Previous 1 is swapped to position 2
[3, 4, 2, 5, 1]
Previous 2 is swapped to position 3
[5, 4, 2, 3, 1]
Previous 3 is swapped to position 4

In [26]: 
    
    Maybe finished by tomorrow. It's likely an x^3 polynomial time algorithm, needs verifiability
    Not finished yet. Thank you Python Software Foundation, MITx, HarvardX and edX.org and Ana Bell, Eric Grimson and John Guttag for teaching me Python at edX.org and MITx
    Thanks National Cryptologic Museum
    Now to work in the factorial of 3 for all non-indexed indices
    Going to need list copies.
"""

def Charles():
    L = [1, 2, 3, 4, 5]
    lL = len(L) - 1
    x = 1
    x <<= lL
    y = x
    c = lL
    d = len(L) - 1
    count = 0
    while d >= 3:
        c = d - 1
        while c >= 0:
#            print("{:05b}".format(x))
#            print("{:05b}".format(y))
            print("Outer loop: {} is swapped with {}".format(d, c))
            count += 1
            c2 = c
            y2 = y
            c2 += 1
            while c2 <= ((len(L) - 1)) and c != d - 1:
                print("Inner loop: {} is swapped with {}".format(c, c2))
                count += 1
                c2 += 1
            y >>= 1
            c -= 1
        d -= 1
    print("Count plus one times five: 5! or len(L) or " +  str((count + 1) * 5))
    print("Needs individual mutation for offset")
if __name__ == """__main__""": Charles()