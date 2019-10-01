# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:33:51 2019

@author: celin
"""

A = float(input())
A = round(A,1)
if (A >= 0 and A <= 10):
    B = float(input())
    B = round(B,1)
    if (B >= 0 and B <= 10):
        C = float(input())
        C = round(C,1)
        if (C >= 0 and C <= 10):            
            pA = 2
            pB = 3
            pC = 5
            med = (pA*A+pB*B+pC*C)/(pA+pB+pC)
            print('MEDIA = %.1f'%med)
        else: print('numero invalido')
    else: print('numero invalido')
else: print('numero invalido')