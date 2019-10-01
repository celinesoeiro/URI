# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:24:19 2019

@author: celin
"""

t = int(input())    # Tempo
v = int(input())    # Velocidade
s = v*t             # Distancia percorrida
kml = 12            # km/l feito pelo veiculo
l = s/kml           # total de litros necessários
print('%.3f'%l) 