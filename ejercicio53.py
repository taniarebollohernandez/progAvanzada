#Exercise 53: Assessing Employees

valor = float(input('Ingrese la calificación:'))


actuación = ''

if valor == 0.0:
    actuacion = 'Inaceptable'
elif valor == 0.4:
    actuacion = 'Aceptable'
elif valor >= 0.6:
    actuacion = ''

if actuacion != '':
	print('Esa no es una calificación válida')
else :
	print('Valor no válido (el valor es 0.0, 0.4 o superior a 0.6)')
if valor== 0.0 or valor== 0.4 or valor >=0.6:
    cantidad= 2400 * valor
 
print('El valor total es:', cantidad)

