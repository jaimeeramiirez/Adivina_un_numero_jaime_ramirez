
import random
num = random.randint(0, 100)
print("\n\n")
nombre_usuario=str(input("Cuál es tu nombre?: "))
print("\nEl número " + str(num) + " es el que debes adivinar")
print("\n\n")
numero_intentos=1
puntuación=0
puntos=0

def juego():
  numero_intentos=1
  while True:
    
    try:
        numero = int(numero)
    except:
        pass
    else:
        if 0 <= numero <= 99:
          break

print("Intente encontrar el número secreto")
print("\n\n")
while True:

    while True:  
        intento = input("Introduzca un número entre 0 y 99: \n")
      
        try:
            intento = int(intento)
        except:
            pass
        else:
            if 0 <= intento <= 99:
                break
              
    if numero_intentos==5:
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
        print("\nHas necesitado", numero_intentos, "intentos\n")
        break

#REGISTRO DE LA PUNTUACIÓN AL FINAL DEL JUEGO
if numero_intentos==1:
    puntuación = puntos + 100
elif numero_intentos==2:
    puntuación= puntos +90
elif numero_intentos==3:
    puntuación=puntos+80
elif numero_intentos==4:
    puntuación=puntos+70
else:
    puntuación= 0

tabla=[nombre_usuario, puntuación]

print(tabla)
juego()
