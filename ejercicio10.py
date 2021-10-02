# Se ingresa una edad, mostrar por pantalla alguna de las siguientes leyendas:
#‘menor’ si la edad es menor o igual a 12  
#‘cadete’ si la edad está comprendida entre 13 y 18
#‘juvenil’ si la edad es mayor que 18 y no supera los 26
#‘mayor’ en el caso que no cumpla ninguna de las condiciones anteriores

edad=int(input("Ingrese su edad: "))

if edad <= 12:
  print("menor")
elif edad <= 18 and edad >= 13:
  print("cadete")
elif edad > 18 and edad <= 27:
  print("juvenil")
else:
  print("mayor")
