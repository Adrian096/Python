#encoding: utf-8

def podzielNa5(np, width):
    i = 0
    napis = np.replace('\n','').replace('\r','')
    nowy_napis = ""
    for x in napis:
        if(i==width):
            nowy_napis += "\n"+x
            i = 0
        else:
            nowy_napis += x
        i+=1

    print(nowy_napis)

f = open("tekst.txt")
dane =  f.read()
f.close()

width = int(input())

podzielNa5(dane, width)

