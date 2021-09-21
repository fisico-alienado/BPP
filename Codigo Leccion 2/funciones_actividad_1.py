from numpy import mean
import pandas as pd
import matplotlib.pyplot as plt


def comprobarTipoInteger(n):
  numeros = []
  for i in n:
    if (type(i) != int):
      try:
        # Para salvar honest mistakes del usuario, como por ejemplo '546'
        i = int(i)
        numeros.append(i)
      except ValueError:
        # Si error en valor, skippearlo y seguir ejecutando el programa
        pass
    else:
      numeros.append(i)
  return numeros

def comprobarNegativoPositivo(n):
  '''
  numeros[0] = números negativos
  numeros[1] = números positivos
  '''
  numeros = [[],[]]
  for i in n:
    if (type(i) != int):
      try:
        # Para salvar honest mistakes del usuario, como por ejemplo '546'.
        i = int(i)
        if (i < 0):
          numeros[0].append(i)
        else:
          numeros[1].append(i)
      except ValueError:
        # Si error en valor, skippearlo y seguir ejecutando el programa
        pass
    else:
      if (i < 0):
        numeros[0].append(i)
      else:
        numeros[1].append(i)
  return numeros

def minimo(n):
  resultado = comprobarTipoInteger(n)
  return min(resultado)

def maximo(n):
  resultado = comprobarTipoInteger(n)
  return max(resultado)

def media(n):
  resultado = comprobarTipoInteger(n)
  return mean(resultado)

def balance_total_mensual(n):
  resultado = comprobarTipoInteger(n)
  return sum(resultado)

def gasto_mensual(n):
  resultado = comprobarNegativoPositivo(n)
  return sum(resultado[0])

def ingreso_mensual(n):
  resultado = comprobarNegativoPositivo(n)
  return sum(resultado[1])