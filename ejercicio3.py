print("Ingrese una serie de numeros enteros, para finalizar ingrese un numero negativo")

numero=int
contador_multiplos_3=0
contador_multiplos_5=0
contador_multiplos_3_5=0

def MCD(A,B):
  R=-1
  while R != 0:
    R = A % B
    if R == 0:
      return B
    else:
      A = B
      B = R

def factorial(numero):
  factorial = 1
  while numero > 1:
    factorial= factorial * numero
    numero = numero - 1
  return factorial 

while numero:

  numero=int(input("Ingrese el numero: "))
  if numero < 0:
    break
  # Calculo su MCD para saber si es multiplo de 3
  multiplo_3= MCD(3,numero)
  # Calculo su MCD para saber si es multiplo de 5
  multiplo_5= MCD(5,numero)

  print("El factorial del numero {0} es {1}".format(numero,factorial(numero)))
  # Dependiendo si son multiplos 3, de 5 o de ambos se van aumentando los contadores
  if multiplo_3 == 3:
    contador_multiplos_3 = contador_multiplos_3 + 1
  if multiplo_5 == 5:
    contador_multiplos_5 = contador_multiplos_5 + 1
  if multiplo_3 == 3 and multiplo_5 == 5:
    contador_multiplos_3_5 = contador_multiplos_3_5 + 1

# Muestro los resultados de los contadores por pantalla
print("En la serie de numeros hay {0} multiplos de 3\nEn la serie de numeros hay {1} multiplos de 5\nEn la serie de numeros hay {2} multiplos de 3 y de 5".format(contador_multiplos_3,contador_multiplos_5,contador_multiplos_3_5)) 
