#Dado el siguiente enunciado, estrategia y representación gráfica especifique los datos de entrada, de salida y  la codificación en Python. Enunciado: Dados dos números, mostrar un menú con opciones de sumar, restar o multiplicar dichos números. Solicite elegir una opción.

# Se inicia la variable en on para que se entre al while
programa="on"

while programa != "off":
  # Ingresando datos 
  n1=int(input("Ingrese el primer numero: "))
  n2=int(input("Ingrese el segundo numero: "))
  
  # menu
  print("1. sumar\n2. restar \n3. multiplicar")
  
  opcion=int(input("Ingrese el numero de la opcion que desea ejecutar: "))

  if opcion == 1:
    suma= n1 + n2
    print("La suma de {0} com {1} es igual a {2}".format(n1,n2,suma))
  elif opcion == 2:
    resta= n1 - n2
    print("La resta de {0} menos {1} es igual a {2}".format(n1,n2,resta))
  elif opcion == 3:
    multiplicacion= n1 * n2
    print("La multiplicación entre {0} y {1} es igual a {2}".format(n1,n2,multiplicacion))
  else:
    print("El numero ingresado no estan en el menú, vuelva a intentarlo")
  
  # se elije la opción para ingresar 
  salida=input("Desea finalizar el programa? S/N").upper()
  if salida == "S":
    programa="off"
