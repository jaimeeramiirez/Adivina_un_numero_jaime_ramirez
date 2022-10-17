
import random
num = random.randint(0, 1000000)
print("\n\n")
nombre_usuario=str(input("Cuál es tu nombre?: "))
#print("\nEl número " + str(num) + " es el que debes adivinar")
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
        if 0 <= numero <= 1000000:
          break

print("Intente encontrar el número secreto")
print("\n\n")
while True:

    while True:  
        intento = input("Introduzca un número entre 0 y 1.000.000: \n")
      
        try:
            intento = int(intento)
        except:
            pass
        else:
            if 0 <= intento <= 1000000:
                break
              
    if numero_intentos==10:
      print("\nHAS UTILIZADO DEMASIADOS INTENTOS, \nGAME OVER")
      print("El número secreto era el:",num)
      
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
elif numero_intentos==5:
    puntuación=puntos+60
elif numero_intentos==6:
    puntuación=puntos+50
elif numero_intentos==7:
    puntuación=puntos+40
elif numero_intentos==8:
    puntuación=puntos+30
elif numero_intentos==9:
    puntuación=puntos+20
else:
    puntuación= 0

print("\n")
tabla=[nombre_usuario, puntuación]

print(tabla)
juego()
