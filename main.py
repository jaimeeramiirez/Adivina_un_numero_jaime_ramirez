print("\n\n\n")
import random 
num = random.randint(0, 100)
print(num)

intento= int(input("Intenta adivinar el número: "))


if (intento>num):
  print("El número que has introducido es mayor que el que tienes que adivinar")
else: print("El número que has introducido es más pequeño que el que tienes que adivinar")



