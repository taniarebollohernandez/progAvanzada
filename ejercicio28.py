import math
T = float(input('Inserte la temperatura del aire en Celsius:'))
V = float(input('Inserte la velocidad del viento en km/hora:'))

A = (T*9/5)+32
B = (V*0.621)

C = (13.21)
D = (0.6215*T)
E = (11.37*V**0.16)
F = (0.3965*T*V**0.16)
WCI = int(C+D+E+F)
print('WCI:', WCI)
