print("\n\n\n")

import random
num = random.randint(0, 100)
print("El número " + str(num) + " es el que debes adivinar")
print("\n\n")
numero_intentos=1

while True:
    # Entramos en un bucle infinito

    # Pedimos introducir un número
    numero = input("Introduzca un número entre 0 y 99 para comenzar el juego: ")


    try:
        numero = int(numero)
    except:
        pass
    else:
        # Hacer la comparación
        if 0 <= numero <= 99:
            # Tenemos lo que queremos, salimos del bucle
            break

# PARTE 2
print("\n")
print("Intente encontrar el número secreto")
print("\n\n")
while numero_intentos<10:
  while True:  # BUCLE 1
    # Entramos en un bucle infinito
    # que permite jugar varios turnos

    while True:  # BUCLE 2
        # Entramos en un bucle infinito
        # que permite corregir un error de escritura
        intento = input("Introduzca un número entre 0 y 99: ")

        try:
            intento = int(intento)
        except:
            pass
        else:
            # Hacer la comparación
            if 0 <= intento <= 99:
                # Tenemos lo que queremos, salimos del BUCLE 2
                break
              
    # Se prueba si el intento es correcto o no
    if intento < num:
      numero_intentos=numero_intentos+1
      print("Demasiado pequeño")
      
    elif intento > num:
      numero_intentos= numero_intentos+1
      print("Demasiado grande")
    elif numero_intentos==10:
      print("HAS UTILIZADO DEMASIADOS INTENTOS")
      break
    else:
        print("Victoria!")
        print("Has necesitado", numero_intentos, "intentos")
        # Terminamos la partida, salimos del BUCLE 1
        break
  break
      