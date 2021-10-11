# 8. Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos: Todos los alumnos mayores de edad y los alumnos mayores (los que tienen más edad)

nombre=""
edad=0

nombres=[]
edades=[]

while nombre != "*":
  nombre = input("Ingrese el nombre del alumno: ")
  # Si el nombre es * se termina el bucle
  if nombre == "*":
    break
  
  # Generamos las validaciones para ir añadiendo los nombres a las listas
  if  len(nombre) >= 3:
    nombres.append(nombre)
    while edad <= 4:
      edad = int(input("Ingrese la edad del alumno {0}".format(nombre)))
      if edad >= 4:
        edades.append(edad)
      else:
        print("El alumno tiene que ser mayor de 4 años")
    edad = 0

  else:
    print("Nombre de alumno invalido, tiene que tener 3 o mas caracteres")
# Inciamos las variables a comparar
alumno_mas_grande=""
edad_alumno_mas_grande=0

# Hacemos un for de i con el rango en el tamaño de los nombres. Hacer un for con una variable que tome los numeros nos va a servir para poder acceder a los indices de las 2 listas
for i in range (len(nombres)):
  # Asignamos a la primera persona como la mayor
  if edad_alumno_mas_grande == 0:
    alumno_mas_grande = nombres[i]
    edad_alumno_mas_grande = edades[i]
  
  # Comparamos las variables mayores
  if edad_alumno_mas_grande < edades[i]:
    alumno_mas_grande = nombres[i]
    edad_alumno_mas_grande = edades[i]
  # Imprimimos si es que el alumno es mayor de edad
  if edades[i] >= 18:
    print("El alumno {0} es mayor de edad".format(nombres[i]))

print("El alumno mas grande es {0} y tiene {1} años".format(alumno_mas_grande,edad_alumno_mas_grande))
