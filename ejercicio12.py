# Escribir un algoritmo, que devuelva el valor absoluto de cualquier valor que reciba.

numero=int(input("Ingrese un numero para saber su valor absoluto: "))

#Evaluamos si se ingreso un numero negativo, en en caso de ser así para obtener su valor absoluto
# tenemos que multiplicarlo por -1, esto le quitara el signo de menos
if numero < 0:
  valor_absoluto= numero * (-1)
else:
  valor_absoluto= numero
# En el caso de ser un valor positivo solo se lo va a asignar a la variable valor_absoluto

print("El valor absoluto de {0} es {1}".format(numero,valor_absoluto))
