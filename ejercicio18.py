# 18. Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:
# Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
# Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
# Eliminar: Me pide una cadena, y la elimina de la lista.
# Mostrar: Muestra la lista de cadenas
# Terminar

palabras = []
salida = "NO"

palabra = "."
print("Ingrese palabras para crear una lista, para terminar de ingresar palabras ingrese una palabra vacia ")

while palabra != "":
  palabra = input("Ingrese la palabra: ")
  if palabra != "":
    palabras.append(palabra)
  else:
    break

print(palabras)

def contar(lista, palabra_a_contar):
  count = 0
  print("Eligio la opción de contar")
  
  for palabra in lista:

    if palabra == palabra_a_contar and palabra_a_contar in lista:
      count = count + 1

  return count

def modificar(lista,palabra,nueva_palabra):
  for i in range(len(lista)):
    if lista[i] == palabra:
      lista[i] = nueva_palabra

def eliminar(lista,palabra):
  lista.remove(palabra)

def mostrar(lista):
  for item in lista:
    print(item)

print("MENU")

while salida != "SI":

  print("Elija una opción:\n1. Contar la cantidad de veces que aparece una palabra\n2. Modificar una palabra por otra\n3. Eliminar una palabra de la lista\n4. Mostrar la lista de palabras\n5. Salir ")

  opcion = int(input("Ingrese la opción: "))

  if opcion == 1:
    palabra_contar = input("Ingresar la palabra para saber cuantas veces se repite")
    veces = contar(palabras,palabra_contar)
    print("La palabra {0} se repitio {1} veces".format(palabra_contar,veces))
  
  if opcion == 2:
    palabra_a_modificar = input("Ingrese la palabra a modificar")
    palabra_para_modificar = input("Ingrese la palabra por la que quiere cambiarla")

    print("La lista antes era:\n{0}".format(palabras))
    modificar(palabras,palabra_a_modificar,palabra_para_modificar)
    print("La lista ahora quedó:\n{0}".format(palabras))

  if opcion == 3:
    palabra_a_eliminar=input("Ingrese la palabra a eliminar")
    
    print("La lista antes era:\n{0}".format(palabras))
    eliminar(palabras,palabra_a_eliminar)
    print("La lista ahora quedó:\n{0}".format(palabras))

  if opcion == 4:
    print("La lista de palabras es: ")
    mostrar(palabras)
    
  if opcion == 5:
    print("Saliendo del programa...")
    break


