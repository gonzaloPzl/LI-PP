import math 
#Importamos el modulo math para usar la función de raiz cuadrada sqrt

raiz=math.sqrt
# le asignamos a la variable raiz la invocación de math.sqrt
print("1. Maximo o minimo de un polinomio de segundo grado\n2. Raices(reales) de un polinomio de segundo grado\n3. La intersección de dos rectas")

opcion=int(input("Escriba el numero de la opcion que desee: "))

if opcion == 1:
  a=int(input("Ingrese el coeficiente a: "))
  b=int(input("Ingrese el coeficiente b: "))
  c=int(input("Ingrese el coeficiente c: "))

  x=  round( -(b/(2*a)), 2 )
  y= round(c - ( (b**2) / (4*a) ), 2 ) 

  if a > 0:
    #maximo porque a es positivo
    print("El maximo del polinomio de grado 2 es ({0},{1})".format(x,y))
  else:
    # minimo porque a es negativo
    print("El minimo del polinomio de grado 2 es ({0},{1})".format(x,y))

# si se elige la opcion 2
elif opcion == 2:
  a=int(input("Ingrese el coeficiente a: "))
  b=int(input("Ingrese el coeficiente b: "))
  c=int(input("Ingrese el coeficiente c: "))

  # Se soluciona la función usando la formula resolvente
  if ( (b**2) - 4*(a*c) ) < 0:
    #Este if comrpueba que la parte de la raiz cuadrada de la formula no sea un numero negativo
    print("No se puede resolver la raiz cuadrada negativa")
  elif a == 0:
    #Comprobamos que la division no se pueda hacer por 0
    print("El valor de a no puede ser 0")
  else:
    # Hacemos la formula resolvente para cada raiz cambiando el signo despues de b
    raiz_positiva= ( -(b) + raiz( b**2 - (4* (a*c) ) ) ) / (2*a)
    raiz_negativa= ( -(b) - raiz( b**2 - (4* (a*c) ) ) ) / (2*a) 

    print("Las raices del polinomio son {0} y {1}".format(raiz_positiva,raiz_negativa))

# si se elige la opcion 3
elif opcion == 3:
  #Datos de la primera recta
  m1=int(input("Ingrese la pendiente de la primera recta: "))
  o1=int(input("Ingrese la ordenada al origen de la primera recta: "))

  #Datos de la segunda recta
  m2=int(input("Ingrese la pendiende de la segunda recta: "))
  o2=int(input("Ingrese la ordenada de la segunda recta: "))

  # Verificamos que las rectas no sean paralelas
  if m1 == m2:
    print("Las rectas son paralelas por lo que no tienen intersección")
  else:
    # Ahora vamos a usar la formula de igualación dividida en pasos

    formula_paso_1= -(m1)+ m2
    #Se separan las pendientes de las ordenandas
    formula_paso_2= o1-(+o2)
    #se despeja la x y se divide el resultado de la suma de ordenadas con la suma de las pendientes
    x= formula_paso_2 / formula_paso_1

    # Con la x encontrada se remplaza en la primera función
    y=(m1*x)+(o1)

    print("El punto de intersección entre las 2 rectas es ({0},{1})".format(round(x, 2),round(y, 2)))

else:
  print("La opción elegida no es válida")
