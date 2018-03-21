import sys

def konwertuj(napis):
    slownik = {}
    for x in napis.split("\n"):
        arguments = x.split(":")
        slownik[arguments[0]] = arguments[1]

    return slownik


napis = ""

with open(sys.argv[1], "r") as f:
    napis = f.read()

print konwertuj(napis)

