class liczbaZespolona:
    liczby = [0, 0]

    def __init__(self, zmienna_1, zmienna_2):
        self.liczby[0] = zmienna_1
        self.liczby[1] = zmienna_2

    def wyswietl(self):
        print("%i + %ii" % (self.liczby[0], self.liczby[1]))

    def __setattr__(self, key, value):
        if(key == "re"):
            self.liczby[0] = value
        elif(key == "im"):
            self.liczby[1] = value
        elif(key == "liczby"):
            self.liczby = [value[0], value[1]]


    def __add__(self, other):
        k_1 = self.liczby[0] + other.liczby[0]
        k_2 = self.liczby[1] + other.liczby[1]
        lZesp = liczbaZespolona(k_1, k_2)
        return lZesp

    def __sub__(self, other):
        k_1 = self.liczby[0] - other.liczby[0]
        k_2 = self.liczby[1] - other.liczby[1]
        lZesp = liczbaZespolona(k_1, k_2)
        return lZesp

    def __mul__(self, other):
        k_1 = (self.liczby[0]* other.liczby[0]) - (self.liczby[0] * other.liczby[0])
        k_2 = (self.liczby[0] * other.liczby[1]) + (self.liczby[1] * other.liczby[0])
        lZesp = liczbaZespolona(k_1, k_2)
        return lZesp

    def __div__(self, other):
        k_1 = ((self.liczby[0] * other.liczby[0]) + (self.liczby[1] * other.liczby[1]))/((other.liczby[0]**2)+(other.liczby[1]**2))
        k_2 = ((self.b * other.liczby[0]) - (self.liczby[0] * other.liczby[1]))/((other.liczby[0]**2)+(other.liczby[1]**2))
        lZesp = liczbaZespolona(k_1, k_2)
        return lZesp

    def modul(self):
        modulZespolony = (self.liczby[0]**2 + self.liczby[1]**2)**0.5
        return modulZespolony

    def __eq__(self, other):
        modulSelf = (self.liczby[0]**2 + self.liczby[1] ** 2)**0.5
        modulOther = (other.liczby[0] ** 2 + other.liczby[1]**2)**0.5
        return modulOther == modulSelf

    def __ge__(self, other):
        modulSelf = (self.liczby[0]**2 + self.liczby[1]**2)**0.5
        modulOther = (other.liczby[0]**2 + other.liczby[1]**2)**0.5
        return modulOther > modulSelf

    def __le__(self, other):
        modulSelf = (self.liczby[0]**2 + self.liczby[1]**2)**0.5
        modulOther = (other.liczby[0]**2 + other.liczby[1]**2)**0.5
        return modulOther < modulSelf


l1 = liczbaZespolona(3.0, 5.0)
l2 = liczbaZespolona(1.0, 2.0)

print(l1.modul())
print(l2.modul())

