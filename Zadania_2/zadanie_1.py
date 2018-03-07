napis = input("Wczytaj napis")

lista = [(slowo, len(slowo)) for slowo in napis.split()]
print(lista)