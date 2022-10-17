print("\n\n\n")

import random
num = random.randint(0, 100)
print("El número " + str(num) + " es el que debes adivinar")
print("\n\n")
numero_intentos=1
def juego():
  numero_intentos=1
  while True:
    
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
print("Intente encontrar el número secreto")
print("\n\n")
while True:  # BUCLE 1
    # Entramos en un bucle infinito
    # que permite jugar varios turnos

    while True:  # BUCLE 2
        # Entramos en un bucle infinito
        # que permite corregir un error de escritura
        intento = input("Introduzca un número entre 0 y 99: \n")
      
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
    if numero_intentos==7:
      print("\nHAS UTILIZADO DEMASIADOS INTENTOS, \nGAME OVER")
      break
    elif intento < num:
      numero_intentos=numero_intentos+1
      print("\nDemasiado pequeño")
      
    elif intento > num:
      numero_intentos= numero_intentos+1
      print("\nDemasiado grande")
    else:
        print("\nVictoria!")
        print("\nHas necesitado", numero_intentos, "intentos")
        break


juego()