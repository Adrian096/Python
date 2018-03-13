import os

sciezka = input("Podaj sciezke do katalogu \n")
rozszerzenie = input("Podaj rozszerzenie \n")

katalogi = os.listdir(sciezka)

for plik in katalogi:
    if plik.endswith(rozszerzenie):
        print(plik)
