
# Implementar algoritmos que permitan: a) Calcular el perímetro de un rectángulo dada su base y su altura. b) Calcular el área de un rectángulo dada su base y su altura. c) Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1, x2, y1, y2. d) Calcular el perímetro de un círculo dado su radio. e) Calcular el área de un círculo dado su radio. f) Calcular el volumen de una esfera dado su radio.g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa. 

# A Perimetro de un rectangulo

import math
#Se importa el modulo math que permite llamar a la constante pi que almacena el valor de pi
salida="N"

while (salida != "S"):
  indice=int(input(" 1.Perimetro de un rectangulo \n 2. Area de un rectangulo \n 4. Permietro de un circulo \n 5. Area de un circulo \n 6. Volumen de una esfera \n 7. Hipotenusa de un triangulo rectangulo \n Ingrese el numero de la opción que desee: "))
  # Se muestra un menu donde el usuario puede elegir los numeros disponibles
  if (indice == 1):
  # Perimetro de un rectangulo
    base=float(input("Ingrese el valor de la base en metros: "))

    altura=float(input("Ingrese el valor de la altura en metros: "))

    perimetro_rectangulo= 2*(base) + 2*(altura)

    print("El perimetro del rectangulo es: ", perimetro_rectangulo, "metros")
  elif (indice == 2):
  # B Área de un rectangulo
    base=float(input("Ingrese el valor de la base en metros: "))

    altura=float(input("Ingrese el valor de la altura en metros: "))

    area_rectangulo=base * altura

    print("El area del rectangulo es: ", area_rectangulo, "metros cuadrados")
  elif (indice == 4):
  # D Perímetro de un círculo dado su radio
    radio_circulo=float(input("Ingrese el radio del circulo en metros: "))

    perimetro_circulo= 2 * math.pi *  radio_circulo

    print("El perimetro del circulo es: ", round(perimetro_circulo, 2), "metros")
    # Se utiliza la función round de python para redondear 2 numeros decimales, se logra pasandole de primer parametro el numero a redondear y el segundo la cantidad de digitos decimales que se quieren tener
  elif (indice == 5):
  # E Área de un circulo con su radio 
    radio_circulo=float(input("Ingrese el radio del circulo en metros: "))

    area_circulo=math.pi*(radio_circulo ** 2)
    # se utiliza la constante math.pi que contiene 3.1415... y se lo multiplica por el resultado del radio a la 2, para hacer una potencia se utiliza "**" antes de la potencia

    print("El area del circulo es: ", round(area_circulo, 2), "metros")
  elif (indice == 6):
  # F Volumen de una esfera dado su radio
    radio_esfera=float(input("Ingrese el radio de la esfera: "))

    volumen_esfera=(4/3)*math.pi*(radio_esfera ** 3)

    print("El volumen de la esfera es:", round(volumen_esfera, 2), "metros")
  elif (indice == 7):
  # G Calcular la hipotenusa de un triangulo rectangulo con sus catetos
    cateto1=float(input("Ingrese el valor del cateto 1 en metros: "))

    cateto2=float(input("Ingrese el valor del cateto 2 en metros: "))

    hipotenusa_al_cuadrado= (cateto1**2) + (cateto2**2)

    hipotenusa= hipotenusa_al_cuadrado**0.5

    print("El valor de la hipotenusa es: ", round(hipotenusa, 2), "metros")
  else:
    print("El numero ingresado es invalido, ingrese un numero disponible en la lista")
  
  salida=input("Desea salir? S/N\n")
  salida = salida.upper()
  # Se pregunta si se desea salir, en el caso de que la respuesta sea "s" se utiliza el método upper para cambiar a mayusculas y que sea consecuente con el programa.










