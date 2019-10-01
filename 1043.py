# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:44:58 2019

@author: celin
"""
import math
a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)

if (a > 0 and b > 0 and c > 0):
    if (a < (b+c) and a > math.fabs(b-c)):
        if (b < (a+c) and b > math.fabs(a-c)):
            if (c < (a+b) and b > math.fabs(a-b)):
                p = a+b+c
                print('Perimetro = %.1f'%p)
    else:
        area = ((a+b)*c)/2
        print('Area = %.1f'%area)
