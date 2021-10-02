#Dados 10 valores informar el mayor

contador=0

numero_mayor=0

# El while va a seguir hasta que el contador llegue a 10
while contador < 10:
  numero=int(input("Ingresar un valor: "))
  if numero_mayor == 0:
    numero_mayor = numero
  elif numero > numero_mayor:
    numero_mayor = numero
  contador= contador + 1

print("El valor mas grande es: {0}".format(numero_mayor))
