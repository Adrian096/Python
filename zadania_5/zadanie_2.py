#encoding: utf-8

def podzielNa5(np, width):
    for index in range(0, len(np), width):
        print(np[index:index+width].center(width))

f = open("tekst.txt")
dane =  f.read()
f.close()

width = int(input())
podzielNa5(dane, width)

