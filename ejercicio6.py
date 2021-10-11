#6. Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

# Hacemos una lista con los meses
meses=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']

# Hacemos una lista con los días, ordenados por los meses
dias= [31,28,31,30,31,30,31,31,30,31,30,31]

numero = 0
while numero <= 0:
  mes = input ("Ingrese el numero del mes para saber la cantidad de días que tiene: ")

  # Validamos que el numero sea uno de los meses
  if mes.isdigit() and int(mes) <= 12 and int(mes) >= 1:
    numero = int(mes)

  else:
    print("El valor ingresado es invalido, ingrese un numero entre el 1 y el 12")

# La clase esta en restarle 1 al indice para que sea la posición correcta, ya que las listas empiezan por el 0 y los meses por le 1
print("El mes {0} tiene {1} días".format(meses[numero - 1], dias[numero - 1]))
