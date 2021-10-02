#Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000 veces, en una única línea, con espacios intermedios. Ayuda: Investigar acerca del parámetro end de la función print

palabra=input("Escribir una palabra para ser escrita 1000 veces: ")

count=0

while count < 1000:
  print(palabra, end=" ")
  count=count+1
#Lo que hace este programa es tener un contador que arranca en 0 y por cada ciclo va a ir aumentando en uno. Se impreme por pantalla lo ingresado por el usuario pasandole al prin la opción de end que concatena los prints que estan pegados en la consola.