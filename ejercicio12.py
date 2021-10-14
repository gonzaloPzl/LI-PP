# 12. Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
# Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.
#   111111111111111
#   100000000000001
#   100000000000001
#   100000000000001
#   111111111111111
# Visualiza el contenido de la matriz en pantalla.

matriz = []

cant_filas = 5
cant_columnas = 15

# Este contador nos va a servir para saber por que fila vamos rellenando
count=0

while len(matriz) < cant_filas:
  sub_matriz = []
  for i in range(cant_columnas):
    # En este caso vamos a agregar 1 si estamos en la posicion 0 de cada lista, si estamos en la ultima o cualquier posicion de la primera y ultima lista
    if i == 0 or i == (cant_columnas - 1) or count == 0 or count == 4:
      sub_matriz.append(1)
    else:
      # Si no se cumple lo anterior iria un 0
      sub_matriz.append(0)
  count = count + 1
  matriz.append(sub_matriz)

# Función para crear la tabla
def crear_tabla(matriz):
  print("TABLA")
  for i in range(len(matriz)):
    for o in range (len(matriz[0])):
      print(matriz[i][o], end=' ')
    print()

crear_tabla(matriz)
