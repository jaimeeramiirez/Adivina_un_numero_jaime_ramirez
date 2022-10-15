print("\n\n\n")

import random
num = random.randint(0, 1000000000000)
print("El número " + str(num) + " es el que debes adivinar")
print("\n\n")
while True:
    # Entramos en un bucle infinito

    # Pedimos introducir un número
    numero = input("Introduzca un número entre 0 y 1000000000000 para comenzar el juego: ")


    try:
        numero = int(numero)
    except:
        pass
    else:
        # Hacer la comparación
        if 0 <= numero <= 1000000000000:
            # Tenemos lo que queremos, salimos del bucle
            break

# PARTE 2
print("Intente encontrar el número a adivinar")
print("\n\n")

while True:  # BUCLE 1
    # Entramos en un bucle infinito
    # que permite jugar varios turnos

    while True:

        intento = input("Introduzca un número entre 0 y 1000000000000 incluídos: ")

        try:
            intento = int(intento)
        except:
            pass
        else:

            if 0 <= intento <= 1000000000000:

                break

    # Se prueba si el intento es correcto o no
    if intento < num:
        print("Demasiado pequeño")
    elif intento > num:
        print("Demasiado grande")
    else:
        print("Victoria!")

        break
