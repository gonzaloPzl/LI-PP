# Dada una serie de M pares {color, número} que corresponden a los tiros de una ruleta. Se pide informar:
# cuántas veces salió el número cero y el número anterior a cada cero
# cuántas  veces seguidas llegó a repetirse el color negro
# cuántas  veces seguidas llegó a repetirse el mismo número y cuál fue
# el mayor número de veces seguidas que salieron alternados el rojo y el negro
# el mayor número de veces seguidas que se negó la segunda docenas

numero=int
color=str
programa=True
color_anterior=""
contador_ceros=0
contador_rojo_negro=0
contador_negros=0
contador_num_repetido=0
contador_mas_repetido=0
numero_repetido=-1
numero_mas_repetido=0
numero_anterior=-1

while programa == True:
  numero=int(input("Ingrese el numero de la ruleta: "))
  if numero >= 0:
    color=input("Ingrese el color correspondiente al numero: ").upper()

    if numero == 0:
      contador_ceros = contador_ceros + 1
      print("El numero 0 salio {0} veces".format(contador_ceros))
      if numero_anterior >= 0:
        print("El numero anterior al 0 es {0}".format(numero_anterior))
    
    # Contador de negros seguidos
    if color_anterior == "NEGRO" and color == "NEGRO":
      contador_negros = contador_negros + 1
    
    # El numero que mas se repitio
    if numero_anterior == numero:
      # Este contador nos sirve para evaluar cuantas veces se repitio el numero que salio mas seguido
      contador_num_repetido = contador_num_repetido + 1
      if numero_repetido == -1:
        numero_repetido = numero
      # Aca se compara el numero mas repetido con el nuevo numero mas repetido
      if contador_mas_repetido < contador_num_repetido:
        numero_mas_repetido = numero
        contador_mas_repetido = contador_num_repetido
        # Reseteo la variable
        contador_num_repetido= 0
    
    # Rojo y negro alterados
    if color_anterior != "" and color_anterior != color and color != "VERDE" and color_anterior != "VERDE":
      print("Entro aca")
      contador_rojo_negro = contador_rojo_negro + 1 
    

    numero_anterior = numero
    color_anterior = color

  else:
    print("La cantidad de veces que llego a repetirse el negro es {0}".format(contador_negros))
    if numero_mas_repetido > 0:
      print("El numero mas repetido es {0} y se repitio {1} veces".format(numero_mas_repetido, contador_mas_repetido))
    print("La cantidad de veces que salieron alterados rojo y negro fueron {0} veces".format(contador_rojo_negro))

    print("[Programa finalizado]")
    # Se cambia a false para que salga del programa
    programa = False
