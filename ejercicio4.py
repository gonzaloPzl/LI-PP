# Dado un conjunto de valores, que finaliza con un valor nulo, determinar e imprimir (si hubo valores):
# a) El valor máximo negativo
# b) El valor mínimo positivo
# c) El valor mínimo dentro del rango -17.3 y 26.9
# d) El promedio de todos los valores.

numero=float

contador = 0 
maximo_negativo = 0
minimo_positivo = 0
minimo_en_rango = 0

suma_total=0
promedio=float

print("Ingrese un conjunto de numeros, para finalizar el ingreso ponga 0")

while numero != 0:
  numero=float(input("Ingrese un numero: "))
  
  # Se el numero es igual a 0 se pone un break que hace terminar el bucle
  if numero == 0:
    break
  
  # si el numero es negativo entra aca
  if numero < 0:
    # Pregunta si la viariable maximo negativo nunca fue sobreescrita y si es así se la asigna al primer numero ingresado
    if maximo_negativo == 0:
      maximo_negativo = numero
    # En el caso de que el numero sea mas grande que el maximo anterior se lo asigna para que sea el nuevo maximo negativo
    if numero > maximo_negativo:
      maximo_negativo = numero
  
  if numero > 0:
    if minimo_positivo == 0:
      minimo_positivo = numero
    if numero < minimo_positivo:
      minimo_positivo = numero
  
  if numero >= -17.3 and numero <= 26.9:
    if numero < minimo_en_rango:
      minimo_en_rango = numero
  
  # Todos los numeros se van sumando para armar un total
  suma_total = suma_total + numero
  # El contador nos va a servir para saber cuantos numeros se ingresaron para sacar el promedio
  contador = contador + 1

promedio = round((suma_total / contador), 2)

if maximo_negativo != 0:
  print("a)El valor máximo negativo es {0}".format(maximo_negativo))
if minimo_positivo != 0:
  print("b)El valor mínimo positivo es {0}".format(minimo_positivo))
if minimo_en_rango != 0:
  print("c) El valor mínimo dentro del rango -17.3 y 26.9 es {0}".format(minimo_en_rango))
print("d) El promedio de todos los valores es {0}".format(promedio))
  