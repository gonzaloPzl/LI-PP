print("Ingresar un numero entero y positivo para calcular su factorial")

num=int(input("Ingrese el numero para calcular el factorial"))

# La función def recibe de parametro el numero
def factorial(numero):
  # La variable factorial empieza con el valor de 1
  factorial = 1
  # Se hace un while para sacar el factorial
  while numero > 1:
    factorial= factorial * numero
    numero = numero - 1
  return factorial

fac = factorial(num)

print("El factorial de {0} es {1}".format(num,fac))
