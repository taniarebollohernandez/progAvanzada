
#ejercicio 9intereses compuestos
# usted acaba de abrir una cuenta de ahorros con el cual gana el 4% de interes por año. El interes que usted genera es pagado al final del año, y es agregado al balance de la cuenta de banco.
# Escriba un programa que comienze a leer la cantidad de dinero depositada en la cuenta (el usuario introduce esta cantidad).
# El programa debe calcular y mostrar la cantidad de dinero en la cuenta despues del primer, segundo y tercer año. Despliegue las cantidades de dinero redondeando a 2 decimales.

a1= float(input('deposito  '))
b1=a1+((4*a1)/100)
print('tiene el año 1 $ %.2f' %b1 )

a2=float(a1+((4*a1)/100))
b2=a2+((4*a2)/100)
print('tiene el año 2 $ %.2f' %b2 )

a3=float(a2+((4*a2)/100))
b3=a3+((4*a3)/100)
print('tiene el año 3 $ %.2f' %b3)


