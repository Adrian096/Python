import sys

def konwertuj(napis):
    slownik = {}
    for x in napis.split("\n"):
        arguments = x.split(" ")
        for arg in arguments:
            if arg in slownik:
                slownik[arg] += 1
            else:
                slownik[arg] = 1

    return slownik


napis = ""

with open(sys.argv[1], "r") as f:
    napis = f.read()

print konwertuj(napis)