import random

numeros = []

def numero_random():
  numero = random.randint(1,10)
  return numero

while len(numeros) < 10:
  numeros.append(numero_random())

print(numeros)

for numero in numeros:
  cuadrado = numero ** 2
  cubo = numero ** 3
  print(cuadrado,cubo)