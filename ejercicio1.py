# Enunciado: a partir de dos valores enteros A y B, informar la suma, la diferencia (A menos B), y el producto.
# Estrategia:
# Solicitar e ingresar datos por teclado
# Calcular suma e informar por monitor
# Calcular diferencia e informar por monitor
# Calcular producto e informar por monitor

# Se ingresa el valor de A
valor_a = int(input("Ingrese el valor A: "))

# Se ingresa el valor de B
valor_b = int(input("Ingrese el valor B: "))

# Se suman los valores y se almacenan en la variable suma
suma= valor_a + valor_b

#Se resta el valor a menos el valor b para almacenarlo en la variable diferencia
diferencia= valor_a - valor_b

#Se hace el producto entre valor a y valor b para guardarlo en la variable producto
producto= valor_a * valor_b

#Se enseñan los valores por pantalla
print("El valor de sumar {0} y {1} es {2}".format(valor_a,valor_b,suma))
print("El resultado de la diferencia entre {0} y {1} es {2}".format(valor_a,valor_b,diferencia))
print("El resultado del producto entre {0} y {1} es {2}".format(valor_a, valor_b,producto))
