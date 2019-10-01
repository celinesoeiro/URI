# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:52:10 2019

@author: celin
"""

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
mAB = int((a + b + abs(a-b))/2)
mBC = int((b + c + abs(b-c))/2)
mAC = int((a + c + abs(a-c))/2)
if (mAB > mBC):
    if (mAB > mAC):
        print(mAB,'eh o maior')
    elif (mAC > mBC):
        print(mAC,'eh o maior')
else: 
    print(mBC,'eh o maior')