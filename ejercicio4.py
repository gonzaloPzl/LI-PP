print("Ingrese el numerador y denominador para obtener todos las simplificaciones posibles")

p= int(input("Ingrese el numerador de la fracción: "))

q= int (input("Ingrese el denominador de la fracción: "))


def MCM(numerador,denominador):
  # Se imprime primero la fraccion que seria igual a una simplificación por 1
  print("{0}/{1}".format(numerador,denominador))
  # Se utiliza la variable reinicio para reiniciar el bucle for
  reinicio = True

  while reinicio:

    # Ponemos variable reinicio en false ya que siempre que el resto de 0 va a entrar al bucle y ponerse en True, entonces cuando no entre porque no hay mas multiplos terminara el while
    reinicio = False
    for i in range(2,10):
      resto1 = numerador % i
      resto2 = denominador % i
      if resto1 == 0 and resto2 == 0:
        numerador = numerador / i
        denominador = denominador / i
        print("{0}/{1}".format(int(numerador),int(denominador)))
        reinicio = True
        break

MCM(p,q)
