import sys

def wczytaj():
    napis = ""
    dane = "none"
    while(dane != ""):
        dane = raw_input()
        if(sys.argv[2] in dane):
            napis += dane + "\n"

    return napis


def wyszukaj():
    f = open(sys.argv[1])
    napis = ""
    for x in f:
        if(sys.argv[2] in x):
            napis += x + "\n"

    return napis



napis = ""
if(sys.argv[1] != "-"):
    napis = wyszukaj()
else:
    napis = wczytaj()

print napis