# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:34:47 2019

@author: celin
"""

A = float(input())
A = round(A,1)
if (A >= 0 and A <= 10):
    B = float(input())
    B = round(B,1)
    if (B >= 0 and B <= 10):
        pA = 3.5
        pB = 7.5
        med = (pA*A+pB*B)/(pA+pB)
        print('MEDIA = %.5f'%med)
    else: print('numero invalido')
else: print('numero invalido')