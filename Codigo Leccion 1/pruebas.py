from numpy import dtype
import pandas as pd
import matplotlib.pyplot as plt

data = {'Enero': ['a',2,3,4,5,6],
        'Febrero': [8,9,1,2,3,1]}

def comprobarTipoInteger(n):
  numeros = []
  for i in n:
    if (type(i) != int):
      try:
        i = int(i)
        numeros.append(i)
      except ValueError:
        pass
    else:
      numeros.append(i)
  return numeros

def minimo(n):
  resultado = comprobarTipoInteger(n)
  return min(resultado)

df = pd.DataFrame(data)
print(df)
print(df.apply(minimo, axis=0))

minimo_columna = df.apply(minimo, axis=0)
minimo_absoluto = min(minimo_columna)
print(minimo_absoluto)

#index_minimo_absoluto = minimo_columna[1].index(1)
print(minimo_columna[1]) # da los values de cada key,value en orden

#Solución para que diga a qué columna pertenece el resultado deseado
for key, value in minimo_columna.items():
  if value == minimo_absoluto:
    print(key,value)

df.plot()
plt.show()






