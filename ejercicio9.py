# 9.Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
# La temperatura media de cada día
# Los días con menos temperatura
# Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.
import random

temp_max_teclado = int
suma_temp_minimas = 0
cont_max_coincidencia=0

temperaturas_maximas = []
temperaturas_minimas = []


# Validamos el ingreso de los datos
while temp_max_teclado == int:
  temp_max_teclado = input("Ingrese una temperatura maxima para saber que días coinciden: ")
  if temp_max_teclado.isnumeric():
    temp_max_teclado = int(temp_max_teclado)
  else:
    print("El dato ingresado no es una temperatura valida")
    temp_max_teclado = int

# Esta función nos va a devolver un numero random
def numero_random():
  numero = random.randint(0,30)
  return numero

while len(temperaturas_maximas) < 5 and len(temperaturas_minimas) < 5:
  # Usamos la función numero random para obtener 2 temperaturas
  temperatura_minima = numero_random()
  temperatura_maxima = numero_random()

  # Si la temperatura minima es mas grande invertimos la lista donde se guarda
  if temperatura_minima > temperatura_maxima:
    temperaturas_maximas.append(temperatura_minima)
    temperaturas_minimas.append(temperatura_maxima)
  # Sino se guarda donde corresponde
  else:
    temperaturas_maximas.append(temperatura_maxima)
    temperaturas_minimas.append(temperatura_minima)

# Sacamos la temperatura media
for i in range(len(temperaturas_maximas)):
  temperatura_media= (temperaturas_minimas[i] + temperaturas_maximas[i]) / 2
  print("La temperatura media del dia {0} es {1}".format(i + 1,temperatura_media))

  # Devolvemos la temperatura maxima si coincide
  if temperaturas_maximas[i] == temp_max_teclado:
    # Aumentamos el contador para saber si hay dias que coincidan
    cont_max_coincidencia += 1
    print("La temperatura maxima del día {0} ({1}) coincide con la ingresada en el teclado".format(i + 1, temp_max_teclado))

  # Suma de las temperaturas medias
  suma_temp_minimas += temperaturas_minimas[i]

promedio_temp_minimas = suma_temp_minimas / len(temperaturas_minimas)

# Si el contador sigue en 0 mostramos el mensaje
if cont_max_coincidencia == 0:
  print("No hay coincidencias con las temperaturas maximas ingresada por teclado")

# Una vez calculada la media podemos determinar que temperaturas minimas se encuentra por debajo de la media
for i in range(len(temperaturas_minimas)):
  if temperaturas_minimas[i] < promedio_temp_minimas:
    print("La temperatura del día {0} es mas baja que la media".format(i + 1))
