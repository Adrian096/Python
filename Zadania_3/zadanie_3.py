class Kolo:
    __srednica = None
    __bieznik = None

    def __init__(self, srednica, bieznik):
        self.__srednica = srednica
        self.__bieznik = bieznik


    def infoKolo(self):
        print("Koło:")
        print("Średnica: ", self.__srednica)
        print("Bieżnik: ", self.__bieznik)

    def zmienKolo(self, srednica, bieznik):
        self.__srednica = srednica
        self.__bieznik = bieznik

    def getSrednica(self):
        return self.__srednica

    def getBieznik(self):
        return self.__bieznik


class Silnik:
    __pojemnosc = None
    __moc = None

    def __init__(self, pojemnosc, moc):
        self.__pojemnosc = pojemnosc
        self.__moc = moc
        self.__predkosc = 0

    def infoSilnik(self):
        print("Silnik:")
        print("Pojemność: ", self.__pojemnosc)
        print("Moc: ", self.__moc)

    def odpalSilnik(self):
        print("Silnik uruchomiony!")

    def getPojemnosc(self):
        return self.__pojemnosc

    def getMoc(self):
        return self.__moc


class Karoseria:
    __kolor = None
    __typ = None


    def __init__(self, kolor, typ):
        self.__kolor = kolor
        self.__typ = typ

    def infoKaroseria(self):
        print("Karoseria:")
        print("Kolor: ", self.__kolor)
        print("Typ: ", self.__typ)

    def otworzDrzwi(self):
        print("Drzwi otwarte!")

    def zmienKolor(self, kolor):
        self.__kolor = kolor

    def getKolor(self):
        return self.__kolor

    def getTyp(self):
        return self.__typ

class Samochod(Silnik, Kolo, Karoseria):
    __marka = None
    __model = None
    __predkosc = None

    def __init__(self, marka, model, pojemnosc, moc, srednica, bieznik, kolor, typ):
        self.__marka = marka
        self.__model = model
        self.__predkosc = 0
        Silnik.__init__(self, pojemnosc, moc)
        Kolo.__init__(self, srednica, bieznik)
        Karoseria.__init__(self, kolor, typ)


    def infoSamochod(self):
        print("Samochód:")
        print("Marka: ", self.__marka)
        print("Model: ", self.__model)
        super().infoKaroseria()
        super().infoKolo()
        super().infoSilnik()

    def odpal(self):
        super().odpalSilnik()

    def zwiekszPredkosc(self, predkosc):
        self.__predkosc += predkosc

    def getMarka(self):
        return self.__marka

    def getModel(self):
        return self.__model

    def getPredkosc(self):
        return self.__predkosc

    def ukradnijAuto(self):
        self.otworzDrzwi()
        self.odpal()
        self.zwiekszPredkosc(120)
        print("Przyspieszono do: ", self.getPredkosc(), "km/h")

sam = Samochod("Opel", "Corsa", "1.5", "105", "14", "Asymetryczny", "Srebrny", "HatchBack")

sam.infoSamochod()
sam.ukradnijAuto()

print(sam)

