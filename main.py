print("\n\n\n")

import random
num = random.randint(0, 100)
print("El número " + str(num) + " es el que debes adivinar")
print("\n\n")

while True:
  
    intento = int(input("Introduzca un número entre 0 y 99 incluídos: "))

    if intento < num:
        print("Prueba con uno más grande")
        print ("\n")

    elif intento > num:
        print("Prueba con uno más pequeño")
        print ("\n")
    else:
        print("ENHORABUENA, HAS ACERTADO!")
        print ("\n")

      
        break
    
#El código funciona, pero no hemos implementado la restricción de números entre 0 y 99, por lo que puedes introducir número mayores a 99 sin que el programa de error. Para que esto no ocurra, tendríamos que introducir otro bucle y que si el usuario introduce un número mayor o menor volver a pedirle que introduzca un número entre 0 y 99.