#1. Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
# Importamos el modulo de random que nos va a servir para los numeros aleatorios
import random

# Inicializamos la lista
lista=[]

# Utilizamos este bucle para formar los 10 numeros
for i in range (10):
  # numero_random va a guardar el valor de un numero aleatorio, a randint se le pasan los parametros entre que 2 numeros oscilaran estos numeros aleatorios
  numero_random= random.randint(1,10)
  # Aplicamos la función append para agregar un elemento a la lista, este elemento esta dentro del parametro y es numero_random
  lista.append(numero_random)

# Iteramos cada numero en la lista
for numero in lista:
  cuadrado=numero**2
  cubo=numero**3
  # Imprimimos el numero, el cuadrado y el cubo
  print("El numero {0} tiene como cuadrado {1} y como cubo {2}".format(numero,cuadrado,cubo))
