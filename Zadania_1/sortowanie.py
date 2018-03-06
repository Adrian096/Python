def sortowanie(tab, kierunek = "rosnaco"): #sortowanie quicksortem
    if(len(tab) <= 1):
        return tab
    pivot = tab[0] #pivot wedlug ktorego porownujemy elementy

    #tablice przechowujace elementy mniejsze, rowne i wieksze od pivota
    mniejsze = []
    wieksze = []
    rowne = []

    #dodajemy do tablic odpowiednie elementy
    for x in tab:
        if(x < pivot):
            mniejsze.append(x)
        elif(x == pivot):
            rowne.append(x)
        else:
            wieksze.append(x)

    #odpowiednio laczymy tablice i je zwracamy
    if(kierunek == "rosnaco"):
        return sortowanie(mniejsze, "rosnaco") + rowne + sortowanie(wieksze, "rosnaco")
    else:
        return sortowanie(wieksze, "malejaco") + rowne + sortowanie(mniejsze, "malejaco")


def sortuj_i_wyswietl(tab, kierunek, zakresDolny, zakresGorny):
    tab = sortowanie(tab, kierunek)
    print(tab[int(zakresDolny):int(zakresGorny)])


tab = []

n = int(input("Podaj ile liczb chcesz wczytac \n"))

print("Podaj "+ str(n) + " liczb")
for i in range(0, n):
    liczba = input()
    tab.append(int(liczba))

kierunek = input("Chcesz sortowac malejaco czy rosnaco, wpisz ('malejaco' lub 'rosnaco') \n")

zakresDolny = input("Zakres dolny wyswietlania tablicy \n")
zakresGorny = input("Zakres gorny wyswietlania tablicy \n")

sortuj_i_wyswietl(tab, kierunek, zakresDolny, zakresGorny)



