def konwertuj(napis):
    slownik = {}
    for x in napis.split("\n"):
        arguments = x.split(":")
        slownik[arguments[0]] = arguments[1]

    return slownik

text = """k1:w1 
k2:w2
k3:w3"""
print konwertuj(text)