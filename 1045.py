# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:05:03 2019

@author: celin
"""

a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)

def triangulos (A,B,C):
    if (A >= (B+C)):
        print('NAO FORMA TRIANGULO')
    else:
        if (A*A == (B*B + C*C)):
            print('TRIANGULO RETANGULO')
        if (A*A > (B*B + C*C)):
            print('TRIANGULO OBTUSANGULO')
        if (A*A < (B*B + C*C)):
            print('TRIANGULO ACUTANGULO')
        if (A == B == C):
            print('TRIANGULO EQUILATERO')
        elif (A == B or A == C or B == C):
            print('TRIANGULO ISOSCELES')

if (a >= 0 and b >= 0 and c >= 0):
    if (a>=b and a>=c):
        if (b>=c):
            A = a; B = b; C = c
            triangulos(A,B,C)
        else:
            A = a; B = c; C = b
            triangulos(A,B,C)
    elif (b>=a and b>=c):
        if (a>=c):
            A = b; B = a; C = c
            triangulos(A,B,C)
        else:
            A = b; B = c; C = a
            triangulos(A,B,C)
    elif (c>=a and c>=b):
        if (a>=b):
            A = c; B = a; C = b
            triangulos(A,B,C)
        else:
            A = c; B = b; C = a
            triangulos(A,B,C)
else:
    print('NAO FORMA TRIANGULO')
