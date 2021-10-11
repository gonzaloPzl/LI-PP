# 4. Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).

print("El programa va a almacenar numeros positivos para luego mostrar la lista generada, si quiere dejar de ingresar datos, ingrese un numero negativo")

lista=[]

numero = 0

while numero >= 0:
  numero = int(input("Ingrese un numero"))

  # Si el numero es negativo salimos del programa
  if numero < 0:
    print("Saliendo del programa")
    break
  # Si el numero es positivo lo agregamos a la lista
  elif numero >= 0:
    lista.append(numero)

# Imprimimos la lista
print(lista)
