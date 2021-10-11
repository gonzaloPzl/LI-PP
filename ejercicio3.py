#3 Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

print("Este programa va a recibir las notas del alumno y va a devolver el promedio, la nota mas baja y la mas alta")

notas=[]

while len(notas) < 5:
  nota = int(input("Ingrese la nota obtenida: "))

  # Si la nota ingresada esta fuera del rango del 0 al 10 lanzamos un error.
  if nota >= 0 and nota <= 10:
    # Si es valido lo añadimos a la lista
    notas.append(nota)
  else:
    print("La nota ingresada es invalida, tiene que ser un numero comprendido entre 0 y 10")

# Inicio las variables para comparar
suma_notas = 0
nota_mas_alta = 0
nota_mas_baja = 0

# Iteramos cada nota dentro de la lista de notas
for nota in notas:
  # Asignamos la primera nota como la mas alta y la mas baja
  if nota_mas_alta == 0:
    nota_mas_alta = nota
  if nota_mas_baja == 0:
    nota_mas_baja = nota
  
  # Comparamos las variables para saber cual es la mas alta y cual la mas baja
  if nota_mas_alta < nota:
    nota_mas_alta = nota
  
  if nota_mas_baja > nota:
    nota_mas_baja = nota
  
  # Cada vuelva vamos a ir sumando las notas
  suma_notas += nota
  
  print("nota: {0}".format(nota))

# Sacamos el promedio con la suma de todas las notas dividido el tamaño de la lista notas.
promedio = suma_notas / len(notas)

print("El promedio de las notas es {0}, la nota mas alta es {1} y la nota mas baja {2}".format(round(promedio, 2), nota_mas_alta, nota_mas_baja))
