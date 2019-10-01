# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 17:00:09 2019

@author: celin
"""

c,q = input().split()
cod = int(c)
quant = int(q)
if (cod == 1):
    val = quant*4.0;
elif(cod == 2):
    val = quant*4.5
elif (cod == 3):
    val = quant*5.0
elif (cod == 4):
    val = quant*2.0
elif (cod == 5):
    val = quant*1.5
else:
    print('codigo errado')
print('Total: R$ %.2f'%val)    