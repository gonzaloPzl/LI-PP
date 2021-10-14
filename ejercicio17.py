# 17. Crear un programa que añada números a una lista hasta que introducimos un número negativo. A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.

print("PROGRAMA:\nAñada a la lista para eliminar los duplicados, para terminar ingrese un numero negativo: ")
lista = []
lista_sin_repetidos = []
num = 0

while num >= 0:
  num = int(input("Ingrese un nuevo numero: "))
  if num < 0:
    # Itera por cada numero en la lista
    for num in lista:
      # Consulta si el ya esta dentro de la lista sin repetidos, en el caso de estar no entra en el if y no se agrega
      if num not in lista_sin_repetidos:
        lista_sin_repetidos.append(num)
    print("Lista original:\n{0}\nLista sin repetidos:\n{1}".format(lista,lista_sin_repetidos))
    print("Saliendo del programa...")
    break
  # Si el valor es mas grande que 0 se añade a la lista
  elif num >= 0:
    lista.append(num)
