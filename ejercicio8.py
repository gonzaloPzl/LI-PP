fecha_teclado = input("Ingrese la fecha: ")
dias_a_sumar = int(input("Ingresar los dias a sumar: "))


def get_annio(fecha):
  annio = ""
  count=0

  for digito in fecha:
    if count < 4:
      annio = annio + digito
    count = count + 1

  return int(annio)

def get_mes(fecha):
  mes = ""
  count = 0
  for digito in fecha:
    if count >= 4 and count < 6:
      mes = mes + digito
    count = count + 1
  return int(mes)
  


def get_dia(fecha):
  dia = ""
  count = 0
  for digito in fecha:
    if count >= 6 and count < 8:
      dia = dia + digito
    count = count + 1
  return int(dia)

print(get_annio(fecha_teclado))
print(get_mes(fecha_teclado))
print(get_dia(fecha_teclado))



def get_dia_del_mes(mes):
  if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    return 31
  elif mes == 2:
    return 28
  elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    return 30

def rutina(annio_fecha, mes_fecha, dia_fecha, dias_a_sumar): #rutina = fecha_nueva
  
  for i in range(dias_a_sumar):
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


  rutina = "{0}/{1}/{2}".format(annio_fecha, mes_fecha, dia_fecha)
  print("{0}/{1}/{2}".format(annio_fecha, mes_fecha, dia_fecha))
  return rutina

rutina(get_annio(fecha_teclado),get_mes(fecha_teclado),get_dia(fecha_teclado), dias_a_sumar)
