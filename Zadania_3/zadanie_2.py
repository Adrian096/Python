class Punkt2D(object):
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def odleglosc(self, punkt):
        odl = ((self.x - punkt.x)**2 + (self.y - punkt.y)**2**2)**0.5
        return odl

class Punkt3D(Punkt2D):
    z = 0

    def __init__(self, x, y, z):
        super(Punkt3D, self).__init__(x, y)
        self.z = z

    def odleglosc(self, punkt):
        odl = ((self.x - punkt.x)**2 + (self.y - punkt.y)**2 + (self.z - punkt.z)**2)**0.5
        return odl


pkt2D_1 = Punkt2D(3, 5)
pkt3D_1 = Punkt3D(2, 6, 3)

pkt2D_2 = Punkt2D(1, 2)
pkt3D_2 = Punkt3D(6, 5, 6)


print(pkt2D_1.odleglosc(pkt2D_2))

