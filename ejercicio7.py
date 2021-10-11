#7. Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

print("Introduzca 5 valores para cada lista para formar una nueva lista mas grande")

# Se inician las listas
lista1 = []
lista2 = []

# Mientras cada lista no tenga 5 valores se ejecuta
while (len(lista1) + len(lista2)) < 10:
  while len(lista1) < 5:
    numero = int(input("Ingrese un valor para la lista 1: "))
    lista1.append(numero)

  while len(lista2) < 5:
    numero = int(input("Ingrese un valor para la lista 2: "))
    lista2.append(numero)

# Se arma una nueva lista que es la suma de las 2 listas anteriores por lo que su tamaño es 10
lista3 = lista1 + lista2

print(lista3)
