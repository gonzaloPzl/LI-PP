# Escribir un programa que tome una cantidad n de valores ingresados por el usuario, a cada uno le calcule el factorial (lo realizado en el ejercicio 1.4) e imprima el resultado junto con el número de orden correspondiente. 

numeros=input("Ingrese los numero separados por coma: ")

array_numeros= numeros.split(",")


for numero in array_numeros:
  factorial=1
  numero = int(numero)
  while numero > 1:
    factorial= factorial * numero
    numero = numero - 1
  print(factorial)
  

