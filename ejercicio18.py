import math

radio = float(input('Inserte el radio del cilindro: '))
altura = float(input('Inserte la altura del cilindro:'))
a = (2*math.pi*radio*(radio+altura))
print('Area  $ %.1f '  %a )