# Dado un triángulo representado por sus lados L1, L2, L3, determinar e imprimir una leyenda según sea: equilátero, isósceles o escálenos.

#Ingreso por pantalla
l1=int(input("Ingrese el lado 1: "))
l2=int(input("Ingrese el lado 2: "))
l3=int(input("Ingrese el lado 3: "))

# Ahora se hace la comprobación de los lados para determinar que tipo de triangulo es
if l1 == l2 == l3:
  print("Es un triangulo equilatero")
elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
  print("Es un triangulo isoceles")
else:
  print("Es un triangulo escaleno")