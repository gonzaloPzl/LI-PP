#Suponiendo que el primer día del año fue lunes, escribir un programa que reciba un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo: si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'.

numero=int(input("Ingrese el día del año, hasta 366"))

# En esta lista ponemos los días, va a estar ordenada de 0 a 6
dias=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
#La condicion para salir del while
salida="N"

#Se comprueba que el numero ingresado sea permitido
if numero <= 0 or numero > 366:
  print("El día ingresado es menor que 1 o mayor que 366")
else:
  while salida!="S":
    # Si el numero es mas grande que 7 se va a ir restando en 7 hasta que dar menor que el mismo
    # Esto lo hacemos para poder acceder al numero del indice
    if numero > 7:
      numero-=7
    else:
      # Con el numero que quedó lo buscamos en el indice para mostrarlo
      dia= dias[numero-1]
      print(dia)
      salida="S"