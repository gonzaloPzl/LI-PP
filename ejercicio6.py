#Se ingresa un conjunto de valores reales, cada uno de los cuales representan el sueldo de un empleado, excepto el último valor que es cero e indica el fin del conjunto. Se pide desarrollar un programa que determine e informe:
#a.Cuántos empleados ganan menos $1.520.
#b.Cuántos ganan  $1.520 o más pero menos de $2.780.
#c.Cuántos ganan $2.780 o más pero menos de $5.999.
#d.Cuántos ganan $5.999 o más.

sueldo=-1

a=0
b=0
c=0
d=0

# Realizamos un while que se termina cuando ingresan 0 y va seccionando cada numero ingresado para aumentar el contador dependiendo el rango
while sueldo != 0:
  sueldo=float(input("Ingrese el sueldo: "))
  if sueldo == 0:
    print("Programa finalizado")
  elif sueldo < 1520:
    a=a+1
  elif sueldo >= 1520 and sueldo < 2780:
    b=b+1
  elif sueldo >= 2780 and sueldo < 5999:
    c=c+1
  elif sueldo >= 5999:
    d=0+1

print("a) Empleados que ganan menos de $1520: {0}\nb) Empleados que ganan de $1520 a $2780: {1}\nc) Empleados que gnan de $2780 a $5999: {2}\nd) Empleados que ganan mas de $5999: {3}".format(a,b,c,d))
