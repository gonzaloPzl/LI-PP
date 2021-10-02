# Enunciado: Dados dos valores enteros y distintos, emitir una leyenda apropiada que informe cuál es el mayor entre ellos.

# Ingreso por de datos
valor1= int(input("Ingresar el primer numero: "))
valor2= int(input("Ingresar el segundo numero: "))

if valor1 == valor2:
  # Se compara si los valores son iguales
  print("Los valores son iguales, ingrese valores diferentes")
elif valor1 > valor2:
  # Se compara que el valor 1 sea mayor que el valor 2, si lo es lo imprime
  print("{0} es mayor que {1}".format(valor1,valor2))
else:
  # Si los numeros no son iguales y el valor 1 no es mayor que el 2 muestra que el valor 2 es mayor que 1 
  print("{0} es mayor que {1}".format(valor2,valor1))
