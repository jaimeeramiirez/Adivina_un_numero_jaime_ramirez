print("\n\n\n")

import random
num = random.randint(0, 100)
nombre_usuario= str(input("Antes de comenzar, introduzca su nombre de usuario: "))
print("\n\n")
print("El número " + str(num) + " es el que debes adivinar")
print("\n\n")
numero_intentos=1
def puntuaciones():
  tabla={}
  tabla["Nombre del jugador"]=input("Introduce un nombre: ")
  tabla["Puntuación: "]=puntuación
  puntos=0
  if numero_intentos==1:
    puntuación = puntos +100
  elif numero_intentos==2:
    puntuación= puntos +90
  elif numero_intentos==3:
    puntuación= puntos +80
  elif numero_intentos==4:
    puntuación= puntos +70
  elif numero_intentos==5:
    puntuación= puntos +60
  elif numero_intentos==6:
    puntuación= puntos +50
  elif numero_intentos==7:
    puntuación= puntos +40
  elif numero_intentos==8:
    puntuación= puntos +30
  elif numero_intentos==9:
    puntuación= puntos +20
  elif numero_intentos==10:
    puntuación= puntos +10
  else:
    puntuación= 0

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
      puntuación=0
      break
    elif intento < num:
      numero_intentos=numero_intentos+1
      print("\nDemasiado pequeño")
      puntuación=puntuación-10
      
    elif intento > num:
      numero_intentos= numero_intentos+1
      print("\nDemasiado grande")
      puntuación=puntuación-10
    else:
        print("\nVictoria!")
        print("\nHas necesitado", numero_intentos, "intentos\n")
        break
      print 
juego()