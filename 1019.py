# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:58:33 2019

@author: celin
"""
#a = b = c = 0
#horas = minutos = segundos = 0
val = int(input())
horas = val // 3600
minutos = (val%3600) // 60
segundos = (val%3600)%60
print('%d:%d:%d'%(horas,minutos,segundos))
