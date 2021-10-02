#Escribir un programa que le pregunte al usuario un número n e imprima los primeros n números triangulares, junto con su índice. Los números triangulares se obtienen mediante la suma de los números naturales desde 1 hasta n. Es decir, si se piden los primeros 5 números triangulares, el programa debe imprimir:
#1 - 1 
#2 - 3 
#3 - 6 
#4 - 10 
#5 - 15 

numero=int(input("Introduzca un numero entero para calcular los triangulares hasta su numero: "))

#
print("Método usando el bucle for:")

triangulares_for=0

for i in range(1, numero + 1):
  triangulares_for= triangulares_for + i
  print(i,"-",triangulares_for)
# Se usa una cuenta parecia a la del factorial solo que sumando

print("Método usando la formula: ")

count=1

while count <= numero:
  triangulares_formula= round((count*(count+1)) / 2)
  print(count,"-",triangulares_formula)
  count=count+1

# El problema resuelto con el ciclo for utiliza menos operaciones.