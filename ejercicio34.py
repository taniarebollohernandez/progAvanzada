# Escriba un programa que lea un numero entero introduciendo pot el usuario.Su programa debe desplegar un mensaje indicando si su numero entero es par o inpar.

entero = float(int(input('Inserte un numero entero:')))

a = (entero / 2)
b = (entero % 2)

if b <= 0.0:
    print('Es un numero par')
elif b >= 1:
    print('Es un numero impar')
