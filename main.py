print("\n\n\n")

print("BIENVENIDO AL FAMOSO JUEGO DE ADIVINA UN NÚMERO \n\nESCOGE TU NIVEL DE DIFICULTAD: ")
print("\n")
print("1. -Nivel simple (del 0 al 100)")
print("2. -Nivel intermedio (del 0 al 1.000)")
print("3. -Nivel avanzado (del 0 al 1.000.000)")
print("4. -Nivel experto (del 0 al 1.000.000.000.000)")
print("\n")
respuesta=input("Elige una opción: ")

if respuesta == "1":
  from nivel_simple import jugar
elif respuesta=="2":
  from nivel_intermedio import jugar
elif respuesta =="3":
  from nivel_avanzado import jugar
elif respuesta =="4":
  from nivel_experto import jugar
else:
  print("ERROR; elegiste una opción no válida")
