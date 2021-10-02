numero=input("Ingrese un año para transformar a romano: ")

romanos={
  1: "I", 2: "II", 3:"III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VII",
  9: "IX", 10: "X"
}

digitos= len(numero)

if digitos == 1:
  numero=int(numero)
  numero_romano=romanos.get(numero)
  print("el numero {0} en numeros romanos es {1}".format(numero,numero_romano))

elif digitos == 2:
  numero=int(numero)