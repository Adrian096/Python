#!/usr/bin/python

from math import *

def rozklad(x):
    tab = []
    int l_p = 2
    
    if(x%l_p == 0):
        tab.append(l_p)
    else:
        l_p = l_p + 1
        

print("Podaj liczbę: ")
l=int(input())
r=rozklad(l)
print r
