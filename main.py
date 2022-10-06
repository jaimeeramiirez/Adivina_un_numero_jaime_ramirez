print("\n\n\n")

import random
num = random.randint(0, 100)
print("El número " + str(num) + " es el que debes adivinar")
print("\n\n")

while True:  # BUCLE 1
  
    intento = int(input("Introduzca un número entre 0 y 99 incluídos: "))

    if intento < num:
        print("Prueba con uno más grande")
    elif intento > num:
        print("Prueba con uno más pequeño")
    else:
        print("ENHORABUENA, HAS ACERTADO!")
      
        break
    

