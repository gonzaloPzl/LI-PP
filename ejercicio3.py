#Dado un conjunto de Nombres y Fechas de nacimientos (AAAAMMDD), que finaliza con un Nombre = ‘FIN’, informar el nombre de la persona con mayor edad y el de la más joven.

nombre=str
fecha=int
mayor_edad = 0
menor_edad = 0
nombre_mayor_edad = str
nombre_menor_edad = str

while nombre != "FIN":
  
  nombre = input("Ingrese el nombre: ").upper()
  
  if nombre == "FIN":
    break

  fecha = input("Ingrese la fecha con el formato AAAAMMDD: ")

  # Manipulo el string de fecha para obtener el año, el mes y el día de forma separada
  anno = int(fecha[0:4])
  mes= int(fecha[4:6])
  dia= int(fecha[6:8])

  # Sumo la multiplicación del año, mes y día obteniendo un numero que mientras mas grande es menor es la persona
  fecha_suma = anno * 10000 + mes * 1000 + dia

  if mayor_edad == 0:
    mayor_edad = fecha_suma
    nombre_mayor_edad = nombre

  if menor_edad == 0:
    menor_edad = fecha_suma
    nombre_menor_edad = nombre

  # Encuentro los mayores y menores y dependiendo el caso le asigno el nombre de la variable nombre_mayor_edad o nombre_menor_edad
  if fecha_suma < mayor_edad:
    mayor_edad = fecha_suma
    nombre_mayor_edad = nombre
  
  if fecha_suma > menor_edad:
    menor_edad = fecha_suma
    nombre_menor_edad = nombre

print("El nombre de la persona mas grande es {0} y el de la menor es {1}".format(nombre_mayor_edad, nombre_menor_edad))
