#ejrcicio 61
#en estwe ejercicio usted creara un programa que calcule el
#promedio de una coleccion de valores insetado por el usuario.
#Si el usuario introduce el valor 0 el programa debe de dejar
#de pedir valores y posteriormente mostrar el promedio calculado





a = 1
sumatoria = 0
i = 0

while a != 0:
    a = int(input('inserte un valor: '))
    sumatoria = sumatoria + a
    i = i + 1

promedio = sumatoria / (i-1)
print('el promedio es: ', promedio)
