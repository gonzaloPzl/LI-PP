# 2. Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

# Incializamos la lista
lista = []

# Mientras el tamaño de la lista sea menor a 5 vamos a pedir que ingresen los datos
while len(lista) < 5:
  # Estos datos seran un string
  string = str(input("Ingrese un string para añadir a la lista: "))

  # Ingresamos los datos en el la lista
  lista.append(string)

# Incializamos la nueva lista
nueva_lista=[]

# Iteramos esta lista desde el 1 hasta el tamaño de la lista + 1, para que i no tome el valor de 0 y llegue hasta le 5
for i in range (1, len(lista) + 1):
  # Le añadimos los elementos a la nueva lista, estos elementos se iran a añadiendo en el orden inverso marcandole el indice negativo de la primera lista
  nueva_lista.append(lista[-i])

print("La lista inversa seria: {0}".format(nueva_lista))
