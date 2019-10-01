# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:37:01 2019

@author: celin
"""
import math
A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)
delta = B*B - (4*A*C)
if (delta < 0 or A == 0):
    print('Impossivel calcular')    
else:
    raiz = math.sqrt(delta)
    r1 = (-B + raiz)/(2*A)
    r2 = (-B - raiz)/(2*A)
    print('R1 = %.5f'%r1)
    print('R2 = %.5f'%r2)
