import sys

def roznice():

    roznice_1 = ""
    roznice_2 = ""
    roznice_1 += "Plik 1\n"
    for x in open(sys.argv[1]):
        if(not(x in open(sys.argv[2]).read())):
            roznice_1 += x

    roznice_2 += "Plik 2\n"
    for x in open(sys.argv[2]):
        if(not(x in open(sys.argv[1]).read())):
            roznice_2 += x

    return roznice_1 + roznice_2



roznice = roznice()

f = open(sys.argv[3], "w")

f.write(roznice)



