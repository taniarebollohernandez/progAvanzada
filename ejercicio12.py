import math


t1 = float(input('Inserta Latitud 01: '))
g1 = float(input('Inserta Longitud 01: '))
t2 = float(input('Inserta Latitud 02: '))
g2 = float(input('Inserta Longitud 02: '))

a1 = math.radians(t1)
a2 =math.radians(g1)
b1= math.radians(t2)
b2 = math.radians(g2)


distancia = 6371.01 * math.acos (math.sin(a1) * math.sin(b1) + math.cos(a1) * math.cos(b1) * math.cos(a2-b2))

print('Distancia km ',distancia)