#Dado el siguiente enunciado y su representación gráfica especifique los datos de entrada, de salida, estrategia, seguimiento y codificación. Enunciado: Dado un número real que representa el importe de una compra informar las posibles formas de pago, según la siguiente tabla:
# 1 cuota  de $................. 
# 2 cuotas de $................. total $................. (   5% de recargo)
# 6 cuotas de $................. total $................. ( 40% de recargo)

importe_de_compra = float(input("Ingrese el importe de la compra para calcular las cuotas: "))

RECARGO_2_CUOTAS= 0.05
RECARGO_6_CUOTAS= 0.4

dos_cuotas = round(((importe_de_compra * RECARGO_2_CUOTAS) + importe_de_compra) / 2, 2)
# Lo hace esta cuenta es primero obtener el 5 porciento del importe de la compra
# para eso multiplica la constante de recargo por el importe para luego suamarlo al importe
# así obtendriamos el importe total con el recargo, luego se divide por la cantidad de cuotas
# por ultimo se le aplica un round para redondear la cuenta

seis_cuotas = round(((importe_de_compra * RECARGO_6_CUOTAS) + importe_de_compra) / 6, 2)

# Mostramos por pantalla las opciones
print("1 cuota de ${0}".format(importe_de_compra))
# Muestro por pantalla la tabla de recargo, se utiliza la constante multiplicada por 100
# Para en el caso de que se cambien los recargos por esas cantidades de cuotas no se modifique esto
#print("2 cuotas de $", dos_cuotas,"(", ,"% de recargo )")
print("2 cuotas de ${0} ({1}% de recargo)".format(dos_cuotas,int(RECARGO_2_CUOTAS*100)))
print("6 cuotas de ${0} ({1}% de recargo)".format(seis_cuotas,int(RECARGO_6_CUOTAS*100)))
