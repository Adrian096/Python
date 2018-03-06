# zadanie_1
imie = input("Podaj imie i nazwisko: ")

wiek = int(input("Ile masz lat? "))

pelnoletni = "niepelnoletni"

if (wiek > 17):
    pelnoletni = "pelnoletni"

print("Cześć " + imie + ", jesteś " + pelnoletni)

# zadanie_2
print("Podaj 3 liczby")

a = int(input("Podaj a:"))

b = int(input("Podaj b:"))

c = int(input("Podaj c:"))

max = a

if (a >= b and a >= c):

    print(a)

elif (b >= a and b >= c):

    print(b)

else:

    print(c)

# zadanie_3
duza = 65

mala = 97

i = 0

while (i <= 25):
    print(chr(mala + i))

    print(chr(duza + i))

    i += 1


# zadanie_4
def alfabet(n):
    duza = 65

    mala = 97

    i = 0

    while (i <= 25):
        print(chr(mala + i))

        print(chr(duza + i))

        i += n


n = int(input("Podaj co ktora litere z alfabetu chcesz wyswietlic:"))

alfabet(n)
alfabet(n)