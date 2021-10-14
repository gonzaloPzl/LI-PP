#10. Diseñar el algoritmo correspondiente a un programa, que:
#Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
#Carga la tabla con valores numéricos enteros.
#Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

import random

matriz = []

cant_filas = 5
cant_columnas = 5

# Se rellena la matriz con numeros randoms
while len(matriz) < cant_filas:
  sub_matriz = []
  for i in range(cant_columnas):
    numero_random = random.randint(1,10)
    sub_matriz.append(numero_random)
  matriz.append(sub_matriz)

def crear_tabla(matriz):
  print("TABLA")
  for i in range(len(matriz)):
    for o in range (len(matriz[0])):
      print(matriz[i][o], end=' ')
    print()

def sumar_filas(matriz):
  suma_fila = 0
  for i in range(len(matriz)):
    for j in range(cant_filas):
      suma_fila = suma_fila + matriz[i][j]
    matriz[i].append(suma_fila)
    suma_fila = 0

def sumar_columnas(matriz):
  nueva_fila=[]
  for i in range(cant_columnas):
    suma = sum([columna[i] for columna in matriz])
    nueva_fila.append(suma)
  matriz.append(nueva_fila)
  # print(nueva_fila)
  # print(matriz)

sumar_columnas(matriz)
sumar_filas(matriz)
crear_tabla(matriz)

