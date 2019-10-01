# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:47:34 2019

@author: celin
"""

n1,n2,n3,n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

med = (2*n1 + 3*n2 + 4*n3 + n4)/(10.0) 
    
print('Media: %.1f'%med)

if (med >= 7.0):
    print('Aluno aprovado.')
elif (med < 5.0):
    print('Aluno reprovado.')
elif (med >= 5.0 and med <= 6.9):
    print('Aluno em exame.')
    n5 = float(input())
    print('Nota do exame: %.1f'%n5) 
    m = (med + n5)/(2.0)
    if (m >= 5.0): 
        print('Aluno aprovado.')
    else: 
        print('Aluno reprovado.')
    print('Media final: %.1f'%m)  

          
