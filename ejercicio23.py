import math
s = float(input('Inserte la longitud de un lado:'))
n = float(input('Inserte numero de lados:'))

a = (n*s*s)
b = math.atan(math.pi/n)

print('Area de el poligono: ', a/4*b)