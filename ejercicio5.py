# Se dispone de un lote de valores enteros positivos que finaliza con un número negativo. El lote está dividido en sublotes por medio de valores cero. Desarrollar un programa que determine e informe:

#a.por cada sublote el promedio de valores
#b.el total de sublotes procesados
#c.el valor máximo del conjunto, indicando en que sublote se encontró y la posición relativa del mismo dentro del sublote
#d.valor mínimo de cada sublote

# Declaración de variables
numero = 1
sublote = 0
cantidad_sublotes = 0
sublote_suma = 0
cant_numeros_sublote = 0
posicion = 0
maximo=0
minimo=0

print("Ingrese numeros enteros positivos, para pasar al siguien sublote ingrese 0, para detenerse ingrese un numero negativo")

while numero >= 0:
  posicion = posicion + 1
  numero=int(input("Ingrese un numero entero positivo: "))
  if numero > 0:
    sublote_suma = sublote_suma + numero
  # Asigno el numero maximo
  if maximo == 0:
    maximo = numero
  
  if numero > maximo:
    maximo = numero
    # Guardamos el lote en el que se encuentra
    sublote_maximo = sublote + 1
    # De esta forma le asignamos la posicion relativa en el sublote
    posicion_en_sublote = posicion

  # El valor minimo de cada sublote
  if minimo == 0:
    minimo = numero
  # Hacemos esta diferencia para que no tome en cuenta el 0 de cada cierre de sublote ni el numero negativo para finalizar.
  if numero < minimo and numero > 0:
    minimo = numero
  

  cant_numeros_sublote= cant_numeros_sublote + 1 

  if numero == 0:
    sublote = sublote + 1
    # A. Muestro el promedio que da el sublote, le restamos 1 al sublote para no tener en cuenta el 0
    promedio_sublote = round((sublote_suma / (cant_numeros_sublote - 1)), 2)

    print("El promedio de los valores dentro del sublote {0} es {1}".format(sublote,promedio_sublote))
    print("El valor minimo del sublote {0} es {1}".format(sublote,minimo))

    # Reseteo las variables para el proximo sublote
    sublote_suma = 0
    cant_numeros_sublote = 0
    posicion=0
    minimo = 0
  
  elif numero < 0:
    sublote = sublote + 1
    # En caso de terminar con un numero negativo para no saltear el sublote lo mostramos
    if cant_numeros_sublote > 1:
      promedio_sublote = round((sublote_suma / (cant_numeros_sublote - 1)), 2)
      print("El promedio de los valores dentro del sublote {0} es {1}".format(sublote,promedio_sublote))
      print("El valor minimo del sublote {0} es {1}".format(sublote,minimo))
    # B. Muestro la cantidad de sublotes procesados
    print("La cantidad de sublotes procesados es: {0}".format(sublote))
    # C. El valor maximo del conjunto, el sublote y la posición relativa en el sublote
    print("El numero maximo es {0} y se encuentra en el sublote {1} en la posición {2}".format(maximo,sublote_maximo,posicion_en_sublote))
