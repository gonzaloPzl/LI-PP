#10. Diseñar el algoritmo correspondiente a un programa, que:
#Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
#Carga la tabla con valores numéricos enteros.
#Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

tabla = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

suma_filas=0

for i in range(len(tabla)):
  for o in range (len(tabla[0])):
    print(tabla[i][o], end=' ')
  print()

