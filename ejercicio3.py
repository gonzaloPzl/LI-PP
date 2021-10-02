# Dados 50 números enteros, informar el promedio de los mayores que 100 y la suma de los menores que –10.
import random

contador=0
num_mayores=0
num_menores=0
contador_mayores=0

# Verifica el tamaño de la lista y si es menor que 50 realiza la itecion
while contador < 50:

  # La randint recibe 2 parametros entre los que va a generar numeros random en un rango
  numero_random= random.randint(-1000, 1000)

  # Si el numero es mayor que 100 entra aca
  if numero_random > 100:
    # Se suman todos los numeros mayores
    num_mayores = num_mayores + numero_random
    # Se contabiliza la cantidad de numeros mayores a 100
    contador_mayores = contador_mayores + 1
  # Si el numero es menor que -10 entra aca
  elif numero_random < -10:
    num_menores = num_menores + numero_random

  # Se saca el promedio  
  promedio = round((num_mayores / contador_mayores), 2)

  contador = contador + 1

print("El promedio de los numeros mayores que 100 es : {0}".format(promedio))

print("La suma de los numeros menores a -10 es: {0}".format(num_menores))
