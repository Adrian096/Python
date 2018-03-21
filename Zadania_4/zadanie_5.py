import sys

def szyfruj(tekst):
    klucz = 3
    szyfr = ""
    for i in range(len(tekst)):
        if((ord(tekst[i]) > 64 and ord(tekst[i]) < 91) or (ord(tekst[i]) > 96 and ord(tekst[i]) < 123)):
            if ord(tekst[i]) > 122 - klucz:
                szyfr += chr(ord(tekst[i]) + klucz - 26)
            else:
                szyfr += chr(ord(tekst[i]) + klucz)
        else:
            szyfr += tekst[i]

    return szyfr

def konwertuj(plik):
    napis = ""

    for x in plik:
        napis += x

    return napis


f = open(sys.argv[1])

napis = konwertuj(f)

szyfr = szyfruj(napis)

f_2 = open(sys.argv[2], "w")

f_2.write(szyfr)

