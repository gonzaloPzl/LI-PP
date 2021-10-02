# Escribir una función que convierta un valor dado en grados Fahrenheit a grados Celsius.

grados_fahrenheit=float(input("Introduzca los grados Fahrenheit para transformar a celcius: "))

grados_celcius=round((grados_fahrenheit - 32) * (5/9), 2)
#Lo relevante es que no se puede usar la formula convencional ya que la variable ingresada por el usuario serian los grados farehenheit, por lo que tenemos que despejar los grados celcius.

print(grados_fahrenheit,"grados Fahrenheit son", grados_celcius,"grados celcius")