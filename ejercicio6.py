
fecha_user=input("Ingrese una fecha con el formato aaaammdd")

def cambiar_formato(fecha):
  # Realizamos un substring de las fechas para obtener cada parte, el dia el mes y el año
  dia=fecha[6:8] 
  mes=fecha[4:6]
  annio=fecha[0:4]

  print("La fecha en formato DD/MM/AA es {0}/{1}/{2}".format(dia,mes,annio))

cambiar_formato(fecha_user)
