print("\n\n\n")

import random
num = random.randint(0, 100)
print("El número " + str(num) + " es el que debes adivinar")
print("\n\n")
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
print("Intente encontrar el número a adivinar")
print("\n\n")

while True:  # BUCLE 1
    # Entramos en un bucle infinito
    # que permite jugar varios turnos

    while True:  # BUCLE 2
        # Entramos en un bucle infinito
        # que permite corregir un error de escritura

        # Pedimos introducir un número
        intento = input("Introduzca un número entre 0 y 99 incluídos: ")

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
        print("Demasiado pequeño")
    elif intento > num:
        print("Demasiado grande")
    else:
        print("Victoria!")
        # Terminamos la partida, salimos del BUCLE 1
        break
