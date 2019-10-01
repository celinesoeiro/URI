# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:37:04 2019

@author: celin
"""

n100 = n50 = n20 = n10 = n5 = n2 = 0
m100 = m50 = m25 = m10 = m5 = m1 = 0

val = float(input())

if (val > 0 and val < 1000000):
    resto100 = val%100
    n100 = (val-resto100)/100
    if (resto100 != 0):
        resto50 = resto100%50
        n50 = (resto100 - resto50)/50
        if (resto50 != 0):
            resto20 = resto50%20
            n20 = (resto50 - resto20)/20
            if (resto20 != 0):
                resto10 = resto20%10
                n10 = (resto20 - resto10)/10
                if (resto10 != 0):
                    resto5 = resto10%5
                    n5 = (resto10 - resto5)/5
                    if (resto5 != 0):
                        resto2 = resto5%2
                        n2 = (resto5 - resto2)/2
                        if (resto2 != 0):
                            resto1 = resto2%1
                            m100 = (resto2 - resto1)/1
                            if (resto1 != 0):
                                resto050 = resto1%0.5
                                m50 = ((resto1 - resto050)/0.5)
                                if (resto050 != 0):
                                    resto025 = resto050%0.25
                                    m25 = ((resto050 - resto025)/0.25)
                                    if (resto025 != 0):
                                        resto010 = resto025%0.1
                                        m10 = ((resto025 - resto010)/0.1)
                                        if (resto010 != 0):
                                            resto005 = resto010%0.05
                                            m5 = ((resto010 - resto005)/0.05)
                                            if (resto005 != 0):
                                                resto001 = round(resto005%0.01)
                                                m1 = round(((resto005 - resto001)/0.01))
print('NOTAS:')
print(int(n100),'nota(s) de R$ 100.00')
print(int(n50),'nota(s) de R$ 50.00')
print(int(n20),'nota(s) de R$ 20.00')
print(int(n10),'nota(s) de R$ 10.00')
print(int(n5),'nota(s) de R$ 5.00')
print(int(n2),'nota(s) de R$ 2.00')
print('MOEDAS:')
print(int(m100),'moeda(s) de R$ 1.00')
print(int(m50),'moeda(s) de R$ 0.50')
print(int(m25),'moeda(s) de R$ 0.25')
print(int(m10),'moeda(s) de R$ 0.10')
print(int(m5),'moeda(s) de R$ 0.05')
print(int(m1),'moeda(s) de R$ 0.01')