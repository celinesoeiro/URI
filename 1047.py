# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:38:18 2019

@author: celin
"""

hi,mi, hf, mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

if (hf>=hi): hora = hf-hi
else: hora = (24-hi) + hf   
    
minutos = mf - mi
if (minutos < 0): 
    hora = hora - 1
    minutos = 60+minutos

# 24h de jogo
if (hi == hf and mi == mf): 
    hora = 24; minutos = 0;
    print('O JOGO DUROU',hora,'HORA(S) E',minutos,'MINUTO(S)')
# De noite para manha: 00:00 até as 24:00 
elif (hi>=0 and mi>=0 and hf<=24 and mf<60): 
    if (hora <= 23 and minutos <= 59):
        print('O JOGO DUROU',hora,'HORA(S) E',minutos,'MINUTO(S)')
    
    



     

