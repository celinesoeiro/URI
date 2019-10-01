# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:34:55 2019

@author: celin
"""

s = float(input())

if (s>=0 and s<=400):
    salarioNovo = s*(1.15);
    reajuste = salarioNovo - s;
    percentual = 15
elif (s>400 and s<=800):    
    salarioNovo = s*(1.12);
    reajuste = salarioNovo - s;
    percentual = 12
elif (s>800 and s<=1200):    
    salarioNovo = s*(1.1);
    reajuste = salarioNovo - s;
    percentual = 10
elif (s>1200 and s<=2000):
    salarioNovo = s*(1.07);
    reajuste = salarioNovo - s;
    percentual = 7
else:    
    salarioNovo = s*(1.04);
    reajuste = salarioNovo - s;
    percentual = 4
    
    
print('Novo salario: %.2f'%salarioNovo)
print('Reajuste ganho: %.2f'%reajuste)
print('Em percentual:',percentual,'%')