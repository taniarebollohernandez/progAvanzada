presion = float(input('Inserte la Presion:'))
volumen = float(input('Inserte el volumen:'))
temperatura = float(input('Inserte la temperatura en kelvin:'))
R = float(8.314) 

n = (presion*volumen/R*temperatura)
print('Numero de moles:' ,' %.2F' %n )