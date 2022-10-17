print("\n\n\n")


print("*"*59)
print("*"*3,"-.BIENVENIDO AL FAMOSO JUEGO DE ADIVINA UN NÚMERO.-","*"*3)
print("*"*59)
print("\n")
print("*"*6,"ESCOGE TU NIVEL DE DIFICULTAD:","*"*6)
print("\n")
print("1. -Nivel simple (del 0 al 100)")
print("2. -Nivel intermedio (del 0 al 1.000)")
print("3. -Nivel avanzado (del 0 al 1.000.000)")
print("4. -Nivel experto (del 0 al 1.000.000.000.000)")
print("\n")
respuesta=input("Elige una opción: (1,2,3 o 4): ")

if respuesta == "1":
  import nivel_simple
elif respuesta=="2":
  import nivel_intermedio
elif respuesta =="3":
  import nivel_avanzado
elif respuesta =="4":
  import nivel_experto
else:
  print("ERROR; elegiste una opción no válida")
