fecha = input("Ingrese la fecha en formato AAAAMMDD: ")

dias_a_sumar = int(input("Ingrese el la cantidad de dias para sumar a la fecha: "))

while not fecha.isdigit():
  print("La fecha ingresada tiene caracteres que no son digitos, ingrese una fecha con el formato AAAAMMDD")
  fecha =input("Ingrese una fecha con numeros en formato AAAAMMDD:")

def get_dia_del_mes(mes):
  if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    return 31
  elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    return 30
  

def sumar_dias(fecha,dias):
  annio_fecha = int(fecha[0:4])
  mes_fecha = int(fecha[4:6])
  dia_fecha = int(fecha[6:8])


  for i in range(dias):
    # Primero le sumo 1 por cada ciclo que tenga el for
    dia_fecha = dia_fecha + 1
    # Consulto si el mes tiene 30, 30 o 28/29 días
    dias_del_mes= get_dia_del_mes(mes_fecha)
    if dias_del_mes == 30:
      # Si el mes tiene 30 días y ya se paso al 3 se suma un mes mas y se resetean los días
      if dia_fecha > 30:
        mes_fecha = mes_fecha + 1
        dia_fecha = 1
    elif dias_del_mes == 31:
      if dia_fecha > 31:
        mes_fecha = mes_fecha + 1
        dia_fecha = 1

    # Si los meses se pasaron de 12 sumo un año y reseteo los meses
    if mes_fecha > 12:
      annio_fecha = annio_fecha + 1
      mes_fecha = 1
  
  print("La fecha obtenida de la suma de {0} días es {1}/{2}/{3}".format(dias_a_sumar,dia_fecha,mes_fecha,annio_fecha))

sumar_dias(fecha,dias_a_sumar)