print("Programa para calcular el maximo común divisor, ingrese los 2 numeros")

A=int(input("Ingrese el primer numero: "))

B=int(input("Ingrese el segundo numero: "))

# Recibe de parametro las variables anteriores que ingreso el usuario
def MCD(A,B):
  # Declaro la variable R(resto) antes de que se utilice
  R=-1
  while R != 0:
    # Saco el resto de los 2 numeros
    R = A % B
    # Cuando la variable resto sea igual que 0 hago el retorno
    if R == 0:
      return B
      # Si no lo es cambio A por B y B por R
    else:
      A = B
      B = R 

print("El maximo comun divisor de {0} y {1} es {2}".format(A,B,MCD(A,B)))
