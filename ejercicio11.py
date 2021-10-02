#  Escribir un algoritmo que resuelvan los siguientes problemas: a) Dado un número entero n, indicar si es par o no. b) Dado un número entero n, indicar si es primo o no. 

numero=int(input("Ingrese un numero entero"))

#Indico si el numero es par o impar usando el mudulo que nos devuelve el resto
# los numeros pares al dividirse por 2 nos dan de resto 0
if (numero % 2) == 0:
  print("El numero {0} es par".format(numero))
else:
  print("El numero {0} es impar".format(numero))

# Para averiguar si es primo vamos a necesitar un contador ya que si es primo
# solo se va a poder dividir arrojando de resto 0 por 1 y por si mismo 
contador=0
for i in range(1, numero+1):
  if (numero % i) == 0:
    contador = contador + 1
# este for va ir desde 1 hasta el numero, se le suma uno porque si no llegaria hasta un
# numero antes que este. Si arroja 0 la division va a sumar 1 al contador

# En el caso de que se ingrese 1, el contador no llegaria a 2 pero tampoco es primo
if numero == 1:
  print("El numero {0} no es primo".format(numero))
  pass
elif contador == 2:
  print("El numero {0} es primo".format(numero))
else:
  print("El numero {0} no es primo".format(numero))


