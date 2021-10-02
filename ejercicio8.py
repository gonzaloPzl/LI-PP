#Enunciado: Dados un mes y el año correspondiente informar cuantos días tiene el mes.

import calendar
# Importamos el modulo de calendario que nos va a servir para comprobar si el año es bisiesto

mes=int(input("Ingrese el numero del mes: "))
anno=int(input("Ingrese el año: "))

# Guardamos en la variable es_bisiesto el valor que nos devuelve isleap cuando le pasamos el año
# esto sera un booleano true si es bisiesto y false sino lo es
es_bisiesto = calendar.isleap(anno)

febrero=28
#Iniciamos febrero que es el unico mes que varia dependiendo el tipo de año

# En el caso de que se haya elegido el mes 2 y el año sea bisiesto se cambia el valor de febrero a 29
if mes == 2 and es_bisiesto:
  febrero = 29

# Se hace un diccionario con los meses como key y la cantidad de dias como el valor
meses = {
  1: 31,2: febrero, 3: 31, 4: 30, 5: 31, 6: 30,
  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# Se imprime el mes usando el método get de los diccionarios que nos devuelve un valor pasandole la key
print("La cantidad de días que tiene el mes {0} son {1}".format(mes,meses.get(mes)))
