# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:53:53 2019

@author: celin
"""

nV = input()        # nome
sV = float(input()) # salário
vV = float(input()) # vendas
p = 0.15
sal = round(((p*vV)+sV),2)
print('TOTAL = R$ %.2f'%sal)