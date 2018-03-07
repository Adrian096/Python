def f1(pkt, kontrolny):
  lista = [(((i[1] - i[0])**2 + (kontrolny[1] - kontrolny[0])**2)**0.5, pkt) for i in pkt]
  return lista
  
lista = [(0, 3), (1, 5), (7, 2)]

print(f1(lista, (3, 1)))