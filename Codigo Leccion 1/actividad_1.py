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

'''
Comprobar que el fichero no está vacío: 

1) Utilizar la función len(), que devuelve el número de elementos de un objeto.
2) Printear el contenido del csv. Aquí se ve que el csv es de 100 rows x 12 columns.
3) Comprobar si el tipo de datos que contiene cada columna es íntegramente de tipo 
   numérico o hay elementos que no van a poder operarse matemáticamente.
'''

csv = pd.read_csv('./finanzas2020.csv', sep='\t', decimal=',', thousands='.')

print('Comprobar elementos del objeto:\n', csv.apply(len, axis=0))

print('\nEl dataframe de las finanzas del 2020 es:\n\n', csv)

print('\nCada columna es de tipo:\n', csv.dtypes)

# Mostrar el mínimo de cada columna; axis = 0 --> se aplica a las COLUMNAS
print('\nEl mayor gasto de cada mes es:\n', csv.apply(minimo, axis=0))

# Mostrar el máximo de cada columna
print('\nEl mayor ingreso de cada mes es:\n', csv.apply(maximo, axis=0))

# Balance por mes = suma de todos los gastos e ingresos por mes
balance_mes = csv.apply(balance_total_mensual, axis=0)
print('\nEl balance total de cada de cada mes es:\n', balance_mes)

# Mes con mejor balance --> Enero
for key, value in balance_mes.items():
  if value == max(balance_mes):
    mes_mas_ahorro_key = key
    mes_mas_ahorro_value = value
    print('\nEl mes con mejor balance es:\n',key,value,'$')

# Mes con peor balance --> Abril
for key, value in balance_mes.items():
  if value == min(balance_mes):
    print('\nEl mes con peor balance es:\n',key,value,'$')

# Gasto totales cada mes
gastos_totales_mes = csv.apply(gasto_mensual, axis = 0)
print('\nLos gastos totales de cada mes son:\n', gastos_totales_mes)
# Mes con mayor gasto total --> Abril
for key, value in gastos_totales_mes.items():
  if value == min(gastos_totales_mes):
    mes_mayor_gasto_key = key
    mes_mayor_gasto_value = value
    print('\nEl mes que más se gastó:\n',key,value,'$')
# Gastos totales año 2020
print('\nGastos totales del 2020:\n', sum(gastos_totales_mes))
# Media de gastos por mes en 2020
media_gasto_mensual = mean(gastos_totales_mes)
print('\nMedia gasto por mes en el 2020:\n', media_gasto_mensual)

# Ingresos totales cada mes
ingresos_totales_mes = csv.apply(ingreso_mensual, axis = 0)
print('\nLos ingresos totales de cada mes son:\n', ingresos_totales_mes)
# Mes con mayores ingresos --> Enero
for key, value in ingresos_totales_mes.items():
  if value == max(ingresos_totales_mes): 
    print('\nEl mes que más se ingresó:\n',key,value,'$')
# Ingresos totales año 2020
print('\nIngresos totales del 2020:\n', sum(ingresos_totales_mes))
# Media de ingresos por mes en 2020
print('\nMedia ingresos por mes en el 2020:\n', mean(ingresos_totales_mes))

# Balance final del año: ingresos menos gastos
gasto_total = sum(gastos_totales_mes)
ingresos_totales = sum(ingresos_totales_mes)
balance_año = ingresos_totales + gasto_total
if (balance_año < 0):
  print('\nBalance total 2020:\n', balance_año, '\n¡Estás endeudado hasta las cejas! Bruce Lee está en camino para cobrarse la deuda.\n')
elif (0 <= balance_año < 10000):
  print('\nBalance total 2020:\n', balance_año, '\nDeberías haber ahorrado más.\n')
else:
  print('\nBalance total 2020:\n', balance_año, '\n¡Bien hecho!\n')

# Una forma condensada y elegante de presentar las respuestas más concretas del ejercicio:

def resumen_finanzas():
  '''
  De la siguiente manera tendríamos 2 filas y 7 columnas
   data = {'Mes con mayor gasto': [mes_mayor_gasto_key],
           'Cantidad (mes mayor gasto)': [mes_mayor_gasto_value],
           'Mes con mayor ahorro': [mes_mas_ahorro_key],
           'Cantidad (mes mayor ahorro)': [mes_mas_ahorro_value],
           'Media gasto mensual': [media_gasto_mensual],
           'Gasto total 2020': [gasto_total],
           'Ingresos totales 2020': [ingresos_totales]}
  '''
  '''
  De esta forma, es más visual y ordenado, con 7 filas y 2 columnas
  '''
  data = {'PREGUNTAS': ['Mes con mayor gasto','Cantidad (mes mayor gasto)','Mes con mayor ahorro','Cantidad (mes mayor ahorro)','Media gasto mensual','Gasto total 2020', 'Ingresos totales 2020'],
          'RESPUESTAS': [mes_mayor_gasto_key,mes_mayor_gasto_value,mes_mas_ahorro_key,mes_mas_ahorro_value,media_gasto_mensual,gasto_total,ingresos_totales]
  }
  return pd.DataFrame(data)

print(resumen_finanzas())

# Evolución ingresos anuales

# Forma 1: Gráfico de línea
ingresos_totales_mes.plot(kind= 'line',title='Evolución de los ingresos en el 2020', xlabel = 'Mes', ylabel = 'Ingresos' )
plt.show()

# Forma 2: Gráfico de barras
ingresos_totales_mes.plot(kind= 'bar',title='Evolución de los ingresos en el 2020', xlabel = 'Mes', ylabel = 'Ingresos' )
plt.show()