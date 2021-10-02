# Escribir un programa que utilice la función anterior para generar una tabla de conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10. 

grados_fahrenheit=0

while grados_fahrenheit < 120:
  grados_fahrenheit=grados_fahrenheit + 10
  grados_celcius=round((grados_fahrenheit - 32) * (5/9), 2)
  print(grados_fahrenheit,"grados fahrenheit son",grados_celcius,"grados celcius")

#Este programa va sumando 10 grados en cada ciclo y sumandoselo a los grandos f