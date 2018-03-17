class LiczbaZespolona(object):
    a = 0
    b = 0

    def __init__(self, zmienna_1, zmienna_2):
        self.a = zmienna_1
        self.b = zmienna_2

    def wyswietl(self):
        print("%i + %ii" % (self.a, self.b))

    def __add__(self, other):
        k_1 = self.a + other.a
        k_2 = self.b + other.b
        l_zesp = LiczbaZespolona(k_1, k_2)
        return l_zesp

    def __sub__(self, other):
        k_1 = self.a - other.a
        k_2 = self.b - other.b
        l_zesp = LiczbaZespolona(k_1, k_2)
        return l_zesp

    def __mul__(self, other):
        k_1 = (self.a* other.a) - (self.a * other.a)
        k_2 = (self.a * other.b) + (self.b * other.a)
        l_zesp = LiczbaZespolona(k_1, k_2)
        return l_zesp

    def __truediv__(self, other):
        k_1 = ((self.a * other.a) + (self.b * other.b))/((other.a**2)+(other.b**2))
        k_2 = ((self.b * other.a) - (self.a * other.b))/((other.a**2)+(other.b**2))
        l_zesp = LiczbaZespolona(k_1, k_2)
        return l_zesp

    def modul(self):
        return (self.a**2 + self.b**2)**0.5

    def __lt__(self, other):
        return (self.modul() < other.modul())

    def __le__(self, other):
        return (self.modul() <= other.modul())

    def __gt__(self, other):
        return (self.modul() > other.modul())

    def __ge__(self, other):
        return (self.modul() >= other.modul())

    def __eq__(self, other):
        return (self.modul() == other.modul())


l1 = LiczbaZespolona(3.0, 5.0)
l2 = LiczbaZespolona(1.0, 2.0)
print(l1.wyswietl())
print(l2.wyswietl())

l3 = l1 + l2
l4 = l1 - l2
l5 = l1 * l2
l6 = l1 / l2

print(l3.wyswietl())
print(l4.wyswietl())
print(l5.wyswietl())
print(l6.wyswietl())

print(l1 < l2)


