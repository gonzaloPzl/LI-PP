# Escribir un programa que le pregunte al usuario una cantidad de pesos, una tasa de interés y un número de años y muestre como resultado el monto final a obtener. La fórmula a utilizar es:
pesos=float(input("Ingrese la cantidad de pesos: "))

tasa_de_interes=float(input("Ingrese la tasa de interes: "))

years=float(input("Ingrese la cantidad de años: "))

cantidad_ahorro= round(pesos * ((1 + (tasa_de_interes / 100)) ** years), 2)


print("El plazo fijo generador en", years, "años es de", cantidad_ahorro,"pesos")
