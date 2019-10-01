# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:39:00 2019

@author: celin
"""
x,y = input().split()

x = float(x)
y = float(y)

if (x>0 and y>0):
    print('Q1')
elif (x>0 and y<0):
    print('Q4')
elif (x<0 and y>0):
    print('Q2')
elif (x<0 and y<0):
    print('Q3')
elif (x==0 and y==0):
    print('Origem')
elif (x == 0 and y != 0):
    print('Eixo Y')
elif (x != 0 and y == 0):
    print('Eixo X')