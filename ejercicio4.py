#  Implementar un algoritmo que, dado un número entero 𝑛, permita calcular su factorial.

numero=int(input("Ingrese un numero entero para calcular el factorial: "))

factorial=1
#Se inicializa el factorial, hay que hacerlo en 1 ya que si inicia en 0 llevara el factorial siempre a 0, y en 1 no se afecta a la multiplicacion
while numero > 1:
  factorial= factorial * numero
  numero = numero - 1
# Lo que sucede es que al ingresar el numero se va a ir multiplicando de forma descendente ya que también se va a ir restando al final de cada ciclo por 1.

print(factorial)
