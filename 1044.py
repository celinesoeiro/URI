# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:00:46 2019

@author: celin
"""

a,b = input().split()
a = int(a)
b = int(b)

if (a%b == 0 or b%a == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')