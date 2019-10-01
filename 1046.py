# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:43:44 2019

@author: celin
"""

h1,h2 = input().split()
h1 = int(h1)
h2 = int(h2)

if (h1 == h2):
    hora = 24
    print('O JOGO DUROU',hora, 'HORA(S)')
elif (h1>=0 and h1<12 and h2>0 and h2<=12): # começou e terminou: Manhã
    hora = h2-h1
    print('O JOGO DUROU',hora, 'HORA(S)')
elif (h1>=0 and h1<12 and h2>12 and h2<=24): #começou manhã, terminou tarde/noite
    hora = h2-h1
    print('O JOGO DUROU',hora, 'HORA(S)')
elif (h1>=12 and h1<24 and h2>=0 and h2<12): #começou tarde/noite, terminou manhã
    hora = (24-h1)+h2
    print('O JOGO DUROU',hora, 'HORA(S)') 

        