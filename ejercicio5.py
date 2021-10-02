#Ingresar e informar valores, mientras que el valor ingresado no sea negativo. Informar la cantidad de valores ingresados.   

valor=int(input("ingresar un valor: "))
valores_totales=0

while valor > 0:

    print(valor)
    valores_totales=valores_totales+1
    print("La cantidad de valores ingresados es {0}".format(valores_totales))

    valor=int(input("ingresar un valor: "))
    
