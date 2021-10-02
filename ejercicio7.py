# Dado un valor M determinar y emitir un listado con los M primeros múltiplos de 3 que no lo sean de 5, dentro del conjunto de los números naturales.

valor=int(input("Ingrese un valor: "))
contador=0
num=0

while contador != valor:
  # Si el numero es multiplo entra 
  if num%3==0:
    # Si el numero no es multiplo de 5 entra
    if num%5!=0:
      print(num)
      # Este contador se aumenta para delimitar la cantidad de numeros que se van a obtener
      contador =contador+1
      
  num=num+1
