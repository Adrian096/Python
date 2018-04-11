#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def pierwiastek(x):
    wynik = None
    try:
        wynik = x**(1.0/2.0)
    except ValueError:
        print("Argument nie może być ujemny!")
    except TypeError:
        print("Niepoprawny typ!")
    except NameError:
        print("Argument powinien być liczbą!")
    return wynik

x = input("Podaj liczbę:\n")

print(pierwiastek(x))
