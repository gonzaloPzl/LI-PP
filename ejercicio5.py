#Implementar algoritmos que resuelvan los siguientes problemas: a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos. b) Dado un número entero n, imprimir su tabla de multiplicar.

salida="N"

while (salida != "S"):
  opcion=int(input("Ingrese el numero de la opción que desee: \n 1. Suma, resta, multiplicacion y division(2 numeros) \n 2. Tabla de multiplicar (1 numero entero)\n"))
  if opcion == 1:
    print("Elegiste 1")
    numero1=float(input("Ingrese el primer numero: "))
    numero2=float(input("Ingrese el segundo numero: "))
    print("El resultado de la suma es: ", numero1+numero2, "\nel resultado de la resta es:", numero1-numero2, "\nEl resultado de la multiplicacion es:",numero1*numero2, "\nEl resultado de la division es:", numero1/numero2 )

  elif opcion == 2:
    numero= int(input("Ingrese el numero para ver su tabla de multiplicar: "))
    for i in range(1, 10):
      tabla = numero * i
      print(numero, "x", i,"=",tabla)
    #Se hace un for hasta el 10 para que sea una tabla hasta el numero 9, luego se multiplica el numero que no varia por la variable i que va a ir tomando el valor del 1 al 9 hasta cumplir todos los ciclos
  else:
    print("La opcion ingresada es incorrecta, elija una opción valida")
  
  salida=input("Desea finalizar el programa? S/N\n")
  salida= salida.upper()




