# Modificar el programa anterior para que pueda generar fichas de un juego quo que puede tener números de 0 a n

fichas=int(input("Ingrese en numero de fichas de su juego: "))

for iz in range(fichas+1):
  for dr in range(iz+1):
    print(iz, "|", dr)
# En este caso solo hay que modifica el valor del rango para que sea variable y lo pueda introducir el usuario