# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:09:18 2019

@author: celin
"""

x = float(input());

s0 = x - 2000.0
i0 = i1 = i2 = 0

if (s0 < 0 or s0 == 0):
    print('Isento')
elif (s0 > 0):
    if (s0 > 0 and s0 <= 1000):
        i0 = s0*0.08;
    else:
        i0 = 1000*0.08;
        s1 = s0 - 1000;
        if (s1 > 0 and s1 <= 1500):
            i1 = s1*0.18;
        else: 
            s2 = s1 - 1500.0;
            i1 = 1500*0.18;
            if (s2 != 0):
                i2 = s2*0.28;
    i = i0 + i1 + i2;
    print('R$ %.2f'%i)    
