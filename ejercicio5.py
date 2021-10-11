# 5. Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.
# Importamos el modulo random para obtener numero aleatorios
import random

# Iniciamos la lista
lista=[]

# Hasta que la lista no tenga 10 elementos seguimos añadiendo
while len(lista) < 10:
  # Int para rendondear solo enteros, random() nos devuelve un numero entre 0 y 1, entonces lo multiplicamos por 100 para obtener entre 0 y 100
  numero = int(random.random() * 100)

  # Añadimos el numero a la lista
  lista.append(numero)

# El método sort lo que hace es ordenar de menor a mayor la lista
lista.sort()

print(lista)
