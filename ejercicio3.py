#Dada una terna de números naturales que representan al día, al mes y al año de una determinada fecha informarla como un solo número natural de 8 dígitos (AAAAMMDD).

dia=int(input("Ingrese el día: "))
mes=int(input("Ingrese el mes: "))
anno=int(input("Ingrese el año: "))

# Se multiplican por 10000 el año y 100 el mes para obtener el formato deseado

mes= mes * 100
anno= anno * 10000
fecha= anno + mes + dia
print("La fecha es {0}".format(fecha))
