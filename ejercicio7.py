print("Ingerse la base y el exponente para obtener la potencia")

b= int(input("Ingrese la base: "))
exp= int(input("Ingrese el exponente: "))

def potencia(base,exponente):
  # Se inicia la potencia en 1, ya que no influye en la multiplicación
  pot=1
  for i in range(exponente):
    # la potencia se genera a partir de multiplicación seguidas
    pot= pot * base
  
  return pot

print("La potencia de la base {0} con el exponente {1} es {2} ".format(b,exp,potencia(b, exp)))
