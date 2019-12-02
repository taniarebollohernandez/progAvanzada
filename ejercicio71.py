# Ejercicio 71

#Escriba un programa que implemente el método de Newton para calcular y mostrar la raíz cuadrada de un número ingresado por el usuario. 

#El algoritmo para el método de Newton sigue:

#Leer x del usuario

#Inicializar adivinar    x / 2

#Mientras que adivinar no es lo suficientemente bueno

#Actualizar conjetura para que sea el promedio de conjetura y x / conjetura

#Cuando se completa este algoritmo, supongo que contiene una aproximación de la raíz cuadrada. 

#La calidad de la aproximación depende de cómo se defina "lo suficientemente bueno". 

#En la solución del autor, la conjetura se consideraba suficientemente buena 

#cuando el valor absoluto de la diferencia entre conjetura ∗ conjetura y x era menor o igual a 10^-12.

import math

def main():

   

  #Input

  x = eval(input("\n Introduzca la raiz cuadrada: "))

  conjetura = eval(input("¿Cuál es tu conjetura?: "))

  #formula

  ans = x ** 1/2

  

  newt = (conjetura + (x / conjetura)) / 2 

  aprox = math.sqrt(x) - newt

  

  #output

  print("\n La raiz cuadra de ", x,"es: ", newt)

  print("la fórmula es", aprox,"precisa")



main()