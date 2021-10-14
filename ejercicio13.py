# 13. De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.
# Para guardar esta información se van a utilizar dos arreglos:
# Nombre: Lista para guardar los nombres de los conductores.
# kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realiza cada conductor.
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

nombres=[]
kms=[]
total_kms=[]
salida = "NO"

print("Programa para añadir kilometros y verificar los recorridos")

def sumar_kms(kms, lista_a_anniadir):
  for i in range(len(kms)):
    suma = sum(kms[i])
    lista_a_anniadir.append(suma)

while salida != "SI":

  print("Que acción desea ralizar? ")

  opcion = int(input("Menu:\n1.Añadir conductor y kilometros en la semana\n2.Visualizar cantidad de kilometros totales de cada conductor"))

  if opcion == 1:
    nombre = input("Ingrese el nombre del conductor: ")
    nombres.append(nombre)
    kilometros = []
    for i in range(7):
      kms_x_dia = int(input("Ingrese la cantidad de kms del día {0}".format(i + 1)))
      kilometros.append(kms_x_dia)
    kms.append(kilometros)

  elif opcion == 2:
    sumar_kms(kms,total_kms)
    for i in range(len(nombres)):
      print("El conductor {0} hizo {1} kms en la semana".format(nombres[i],total_kms[i]))

  salida = input("Desea salir del programa? SI/NO : ").upper()

