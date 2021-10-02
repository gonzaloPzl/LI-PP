#Dados N y M números naturales, informar su producto por sumas sucesivas.

numero_n=int(input("Ingresar el primer numero natural: "))
numero_m=int(input("Ingresar el segundo numero natural: "))

suma=0
# Verificamos que se haya ingresado un numero natural
if numero_n < 0 or numero_m < 0:
  print("El numero ingresado no es un numero natural")
else:
  # Iteramos la cantidad de veces que sea el segundo numero
  for i in range(numero_m):
    # Esa cantidad de veces es la que se va a sumar el primer numero
    suma=suma+numero_n
  
  print("El resultado de la multiplicación es: {0}".format(suma))
