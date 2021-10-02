#A partir de un valor entero ingresado por teclado, se pide informar:
#a. La quinta parte de dicho valor
#b. El resto de la división por 5
#c. La séptima parte del resultado del punto a)

numero=int(input("Ingrese un numero entero: "))

# La quinta parte de dicho valor
quinta_parte= (numero / 5)

# El resto de la vision por 5
resto= round(numero % 5, 2)

# La séptima parte del resultado del punto a)
septima_parte= round(quinta_parte / 7, 2)

print("a) La quinta parte de dicho valor: {0}".format(quinta_parte))
print("b) El resto de division por 5: {0}".format(resto))
print("c) La séptima parte del resultado del punto a): {0}".format(septima_parte))
