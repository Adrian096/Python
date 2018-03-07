import os, sys

sciezka = input("Podaj sciezke do katalogu \n")
rozszerzenie = input("Podaj rozszerzenie")

katalogi = os.listdir(sciezka)

for plik in katalogi:
  print(plik)