#escribir un programa que determine si una palabra determinada por el programa es palindromo o no lo es. Un palindromo es una palabra que se lee igual de izquierda a derecha, que de derecha a izquierda, por ejemplo
#RADAR
#ROTOR
#RAYAR
#SOMETEMOS
#funcion apend
igual, aux = 0, 0
texto = input("Ingrese la palabra: ")
for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    igual += 1
  aux += 1
if len(texto) == igual:
  print("Es palindromo!")
else:
  print("No es palindromo!")