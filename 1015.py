# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:46:04 2019

@author: celin
"""
import math
x1,y1 = input().split()
x2,y2 = input().split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
a = (x2-x1)**2
b = (y2-y1)**2
d = math.sqrt(a+b)
print('%.4f'%d)