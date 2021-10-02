# Escribir un programa que imprima por pantalla todas las fichas de dominó, de una por línea y sin repetir. 

for iz in range(7):
  for dr in range(iz+1):
    print(iz,"|",dr)

# Para poder imprimir el dominó se hace un rango hasta el 7, incluyendo el 0 ya que hay fichas con ese valor. Luego cada vez que entre en el ciclo va a entrar a otro que va a ser el de la derecha que va a ir hasta el numero de la izquierda.