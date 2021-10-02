#Dadas dos fechas informar cual es la más reciente. Determine cuáles serían los datos de entrada  y las leyendas a informar de acuerdo al proceso solicitado.
primera_fecha= input("Ingrese la primera fecha con el formato DD/MM/AAAA")
segunda_fecha= input("Ingrese la segunda fecha con el formato DD/MM/AAAA")

# Fecha 1
# Hacemos una lista a partir de la primera fecha, diviendo por dia, mes y año
lista_fecha_1 = primera_fecha.split("/")
# Se inicia la suma
suma_total_1 = 0

# Se inicia el multiplicador que va a añadir importancia decreciente para que los meses y dias no valgan lo mismo
multiplicador_1=1

for fecha in lista_fecha_1:
  # se van sumando los dias con los meses y años multiplicados por la importancia de los mismos
  # esto evitara que meses mas recientes pero dias mas altos generen problemas
  if len(fecha) == 4:
    suma_total_1 = suma_total_1 + ( int(fecha) * 1000)
  suma_total_1 = suma_total_1 + (int(fecha) * multiplicador_1)
  multiplicador_1= 100


# Fecha 2
lista_fecha_2 = segunda_fecha.split("/")
suma_total_2 = 0

multiplicador_2=1

for fecha in lista_fecha_2:
  if len(fecha) == 4:
    suma_total_2 = suma_total_2 + ( int(fecha) * 1000)
  suma_total_2 = suma_total_2 + (int(fecha) * multiplicador_2)
  multiplicador_2= 100


# se comparan los numeros de las sumas de las 2 fechas para saber cual es mas reciente.
if suma_total_1 > suma_total_2:
  print("La fecha {0} es mas reciente que la fecha {1}".format(primera_fecha,segunda_fecha))
elif suma_total_1 == suma_total_2:
  print("Las fechas son iguales")
else:
  print("La fecha {0} es mas reciente que la fecha {1}".format(segunda_fecha,primera_fecha))
