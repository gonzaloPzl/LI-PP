#Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

numero1=int(input("Introduzca el primer numero: "))
numero2=int(input("Introduzca el segundo numero: "))

if numero1 < numero2:
  n1=numero1
  n2=numero2

  for i in range(n1, n2):
    if i % 2 == 0:
      print(i)
elif numero1 == numero2:
  print("Los numero son iguales, no se pueden encontrar numeros pares intermedios")
elif numero1 > numero2:
  n1= numero2
  n2= numero1

  for i in range(n1, n2):
    if i % 2 == 0:
      print(i)

# Lo if sirven para comprobar si los valores son adecuados para realizar una division correcta, si el segundo numero es mas grande que el primero se invierten
# El operador % modulo sirve para obtener el resto, por lo que si se hace la vision y el resto es 0 entonces se imprime en pantalla porque es un numero par.

