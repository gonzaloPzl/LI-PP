# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
# Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
# Muestra el contenido de la tabla en pantalla.

matriz = []

cant_filas = 5
cant_columnas = 5

count=0

while len(matriz) < cant_filas:
  sub_matriz = []
  for i in range(cant_columnas):
    if i == count:
      sub_matriz.append(1)
    else:
      sub_matriz.append(0)
  count = count + 1
  matriz.append(sub_matriz)

def crear_tabla(matriz):
  print("TABLA")
  for i in range(len(matriz)):
    for o in range (len(matriz[0])):
      print(matriz[i][o], end=' ')
    print()

crear_tabla(matriz)
