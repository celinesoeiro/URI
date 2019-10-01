# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:31:04 2019

@author: celin
"""

a = b = c = d = e = f = g = 0
a1 = b1 = c1 = d1 = e1 = f1 = g1 = 0

val = int(input())
if (val > 0 and val < 1000000):
    a = val%100; a1 = (val-a)/100
    if (a != 0):
        b = a%50; b1 = (a-b)/50
        if (b != 0):
            c = b%20; c1 = (b-c)/20
            if (c != 0):
                d = c%10; d1 = (c-d)/10
                if (d != 0):
                    e = d%5; e1 = (d-e)/5
                    if (e != 0):
                        f = e%2; f1 = (e-f)/2
                        if (f != 0):
                            g = e%1 
                            g1 = (f-g)/1
print(val)
print(int(a1),'nota(s) de R$ 100,00')
print(int(b1),'nota(s) de R$ 50,00')
print(int(c1),'nota(s) de R$ 20,00')
print(int(d1),'nota(s) de R$ 10,00')
print(int(e1),'nota(s) de R$ 5,00')
print(int(f1),'nota(s) de R$ 2,00')
print(int(g1),'nota(s) de R$ 1,00')