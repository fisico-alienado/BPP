import funciones_actividad_1
import pandas as pd
import pytest

data_prueba = {'Enero': ['a',2,3,4,-5,6],
               'Febrero': [8,-9,1,-2,3,1]}

df = pd.DataFrame(data_prueba)

def test_comprobarTipoInteger():
  prueba = df.apply(funciones_actividad_1.comprobarTipoInteger, axis=0)
  resultado = {'Enero': [2,3,4,-5,6],
               'Febrero': [8,-9,1,-2,3,1]}
  caso_1 = prueba['Enero'] == resultado['Enero']
  caso_2 = prueba['Febrero'] == resultado['Febrero']
  assert caso_1
  assert caso_2
  
def test_comprobarNegativoPositivo():
  prueba = df.apply(funciones_actividad_1.comprobarNegativoPositivo, axis=0)
  resultado = {'Enero': [[-5],[2,3,4,6]],
               'Febrero': [[-9,-2],[8,1,3,1]]}
  caso_1_1 = prueba['Enero'][0] == resultado['Enero'][0]
  caso_1_2 = prueba['Enero'][1] == resultado['Enero'][1]
  caso_2_1 = prueba['Febrero'][0] == resultado['Febrero'][0]
  caso_2_2 = prueba['Febrero'][1] == resultado['Febrero'][1]
  assert caso_1_1
  assert caso_1_2
  assert caso_2_1
  assert caso_2_2

def test_minimo():
  prueba = df.apply(funciones_actividad_1.minimo, axis=0)
  resultado = {'Enero': [-5],
               'Febrero': [-9]}
  caso_1 = prueba['Enero'] == resultado['Enero']
  caso_2 = prueba['Febrero'] == resultado['Febrero']
  assert caso_1
  assert caso_2
  
def test_maximo():
  prueba = df.apply(funciones_actividad_1.maximo, axis=0)
  resultado = {'Enero': [6],
               'Febrero': [8]}
  caso_1 = prueba['Enero'] == resultado['Enero']
  caso_2 = prueba['Febrero'] == resultado['Febrero']
  assert caso_1
  assert caso_2

def test_media():
  prueba = df.apply(funciones_actividad_1.media, axis=0)
  resultado = {'Enero': [2],
               'Febrero': [0.3333333333333333]}
  caso_1 = prueba['Enero'] == resultado['Enero']
  caso_2 = prueba['Febrero'] == resultado['Febrero']
  assert caso_1
  assert caso_2

def test_balance_total_mensual():
  prueba = df.apply(funciones_actividad_1.balance_total_mensual, axis=0)
  resultado = {'Enero': [10],
               'Febrero': [2]}
  caso_1 = prueba['Enero'] == resultado['Enero']
  caso_2 = prueba['Febrero'] == resultado['Febrero']
  assert caso_1
  assert caso_2

def test_gasto_mensual():
  prueba = df.apply(funciones_actividad_1.gasto_mensual, axis=0)
  resultado = {'Enero': [-5],
               'Febrero': [-11]}
  caso_1 = prueba['Enero'] == resultado['Enero']
  caso_2 = prueba['Febrero'] == resultado['Febrero']
  assert caso_1
  assert caso_2

def test_ingreso_mensual():
  prueba = df.apply(funciones_actividad_1.ingreso_mensual, axis=0)
  resultado = {'Enero': [15],
               'Febrero': [13]}
  caso_1 = prueba['Enero'] == resultado['Enero']
  caso_2 = prueba['Febrero'] == resultado['Febrero']
  assert caso_1
  assert caso_2
