import pdb
pdb.set_trace()

# 1. Haciendo uso de comprensión de listas realice un programa que, dado una lista de listas de números enteros, devuelva el máximo de cada lista.

lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
maximos = [max(i) for i in lista]
print(maximos)

# 2. Haga uso de la función filter para construir un programa que, dado una lista de n 
#    números devuelva aquellos que son primos. 

# Como lo haría SIN utilizar Filter
def es_primo(r):
  contador = 0
  almacen = []
  for e in r:
    primo = True
    for i in range(2,e):
      if (e%i == 0):
        primo = False
    if primo:
      almacen.append(e)
      contador += 1
  return almacen

lista_2 = [3, 4, 8, 5, 5, 22, 13, 15, 127]

print(es_primo(lista_2))

# Utilizando filter. Filter hace la función "for e in r" en la función es_primo. 
# Como se ve, nos ahorramos unas cuantas líneas de código.
def es_primo_2(e):
  primo = True
  for i in range(2,e):
    if (e%i == 0):
      primo = False
  return primo

primos = list(filter(es_primo_2, lista_2))

print(primos)