# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 14:24:45 2019

@author: celin
"""
A,B,C,D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)
p = A%2
s1 = C+D
s2 = A+B
if (p == 0 and s1>s2 and C>0 and D>0 and B>C and D>A):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')