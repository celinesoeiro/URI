# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:21:06 2019

@author: celin
"""

A,B,C = input().split()
A = round(float(A),1)
B = round(float(B),1)
C = round(float(C),1)
pi = 3.14159
a = (A*C)/2
b = pi*C*C
c = (A+B)*C/2
d = B*B
e = A*B
print('TRIANGULO: %.3f'%a)
print('CIRCULO: %.3f'%b)
print('TRAPEZIO: %.3f'%c)
print('QUADRADO: %.3f'%d)
print('RETANGULO: %.3f'%e)