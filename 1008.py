# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 19:44:21 2019

@author: celin
"""

nE = int(input())    # numero do empregado
hE = int(input())  # horas trabalhadas 
phE = float(input()) # preco da hora
sal = round((hE * phE),2)
print('NUMBER =',nE)
print('SALARY = U$ %.2f'%sal)
