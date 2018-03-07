def f1(n):
  if(n%2 == 0):
    return True
  else: 
    return False
    
def f2(f, l):
  tab = []
  for i in l:
    if(f(i) == True):
      tab.append(i)
  return tab
      
n = [0, 1, 2, 3, 4, 5, 6, 8, 11, 13]

tab = f2(f1, n)
print(tab)