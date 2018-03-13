n = int(input("Podaj n \n"))

tab_1 = [1, 1]

[tab_1.append(tab_1[x] + tab_1[x-1]) for x in range(1, n)]

print(tab_1)