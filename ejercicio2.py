# Dados N valores informar el mayor, el menor y en que posición del conjunto fueron ingresados

numero_mayor = 0
numero_menor = 0
posicion_mayor = 0
posicion_menor = 0
salida= "N"

posicion=0

print("Ingrese valores para saber cual es el mayor, el menor y su posición")

while salida != "S":
  # Va a ir tomando el valor de cada ciclo para así saber la posicion en la que se ingrese el mayor o el menor
  posicion = posicion + 1
  numero=int(input("Ingrese un valor: "))

  # Le asigno en el primer ciclo el numero mayor y menor al correspondiente ya que el primer numero siempre sera el mayor y el menor

  if numero_mayor == 0:
    numero_mayor = numero
    posicion_mayor = posicion

  if numero_menor == 0:
    numero_menor = numero
    posicion_menor = posicion

  # Obteniendo el numero mayor
  if numero > numero_mayor:
    numero_mayor = numero
    posicion_mayor = posicion
  
  # Obteniendo el numero menor
  elif numero < numero_menor:
    numero_menor = numero
    posicion_menor = posicion
  
  # Le pregunto al usuario si desea finalizar con el programa
  salida = input("Desea salir del programa? S/N ").upper()

print("El valor mas alto es {0} y fue ingresado en la posicion {1}. El valor mas bajo es {2} y fue ingresado en la posicion {3}.".format(numero_mayor,posicion_mayor,numero_menor,posicion_menor))
