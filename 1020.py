# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:06:56 2019

@author: celin
"""
anoResto = mesResto = 0
ano = mes = dias = 0
val = int(input())
a = 365
m = 30
anoResto = val%a
if (anoResto != 0):
    ano = int((val-anoResto)/a)
    mesResto = anoResto%m
    if (mesResto != 0):
        mes = int((anoResto - mesResto)/m)
        dias = int(mesResto)
    else: 
        mes = int(val/m)
else:
    ano = int(val/a)
print(ano,'ano(s)')
print(mes,'mes(es)')
print(dias,'dia(s)')