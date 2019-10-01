# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:03:24 2019

@author: celin
"""

vX = 1      # 1km/min
vY = 1.5    # 1.5km/min
dist = int(input())
dv = vY - vX    # Diferença entre as velocidades
tempo = int(dist/dv) # Calculando o tempo
print(tempo,'minutos')
