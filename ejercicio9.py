print("El programa te devolvera la suma de 2 tiempos determinados")

hora=input("Ingrese la hora en el formato HHMMSS: ")

tiempo=input("Ingrese el tiempo para sumar a la hora en el formato HHMMSS: ")
  

def sumar_hora(hora, tiempo):
  # Separamos las horas, minutos y segundos
  hora_hora= int(hora[0:2])
  minutos_hora= int(hora[2:4])
  segundos_hora = int(hora[4:6])

  # Separamos las horas, minutos y segundos a sumar
  hora_tiempo= int(tiempo[0:2])
  segundos_tiempo = int(tiempo[4:6])
  minutos_tiempo= int(tiempo[2:4])

  # Empezamos a sumar los segundos
  segundos_suma = segundos_hora + segundos_tiempo
  # Si los segundos son mas de 60 lo restamos por 60 y le añadimos un minuto, no importa a que variable de minuto, si a minuto_hora o a minuto_tiempo
  if segundos_suma > 60:
    segundos_suma = segundos_suma - 60
    minutos_tiempo = minutos_tiempo + 1
  
  minutos_suma = minutos_hora + minutos_tiempo

  if minutos_suma > 60:
    minutos_suma = minutos_suma - 60
    hora_tiempo = hora_tiempo + 1
  
  hora_suma = hora_hora + hora_tiempo
  # En el caso de la hora si es mayor o igual que 24 la restamos por 24 y no le sumamos a nadie ya que el que cambia es el día
  if hora_suma >= 24:
    hora_suma = hora_suma - 24
  
  print("La hora generada por la suma de {0} y {1} es {2}:{3}:{4}".format(hora, tiempo, hora_suma,minutos_suma,segundos_suma))

sumar_hora(hora,tiempo)


# fecha="19991226"

# annio=""
# mes=""
# dia=""

# count=0

# for digito in fecha:
#   if count < 4:
#     annio = annio + digito
  
#   elif count < 6:
#     mes = mes + digito
  
#   elif count < 8:
#     dia = dia + digito
  
#   count = count + 1

# print("El dia es {0}, el mes {1} y el año {2}".format(dia,mes,annio))