# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:46:50 2019

@author: celin
"""

filo = input() #vertebrado ou invertebrado
classe = input() #ave, manifero, inseto ou anelideo
alimentacao = input() #carnivoro, onivoro, herbivoro ou hematofogo

if (filo == 'vertebrado'):
    if (classe == 'ave'):
        if (alimentacao == 'carnivoro'):
            print('aguia')
        if (alimentacao == 'onivoro'):
            print('pomba')
    if (classe == 'mamifero'):
        if (alimentacao == 'onivoro'):
            print('homem')
        if (alimentacao == 'herbivoro'):
            print('vaca')
if (filo == 'invertebrado'):
    if (classe == 'inseto'):
        if (alimentacao == 'hematofago'):
            print('pulga')
        if (alimentacao == 'herbivoro'):
            print('lagarta')
    if (classe == 'anelideo'):
        if (alimentacao == 'hematofago'):
            print('sanguessuga')
        if (alimentacao == 'onivoro'):
            print('minhoca')

            