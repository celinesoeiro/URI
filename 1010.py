# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:00:02 2019

@author: celin
"""
cP1,nP1,pP1 = input().split()
cP1 = int(cP1)
nP1 = int(nP1)
pP1 = round(float(pP1),2)
cP2,nP2,pP2 = input().split()
cP2 = int(cP2)
nP2 = int(nP2)
pP2 = round(float(pP2),2)
val = nP1*pP1 + nP2*pP2
print('VALOR A PAGAR: R$ %.2f'%val)

