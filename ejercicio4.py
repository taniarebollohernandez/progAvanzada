#Crear un programa quelea el largo y el ancho de un campo de cultivo, introducido por el usuario y despliegue el area del campo.

largo = float(input('Introduce el largo del campo en metros'))

ancho = float(input('Introduce el ancho del campo en metros'))

metro = float(0.00247105)
print('El area del campo es de', (largo*ancho*metro),'acres')
