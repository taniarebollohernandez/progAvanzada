import math
s1 = float(input('Inserte longitud1 del triangulo:'))
s2 = float(input('Inserte longitud2 del triangulo:'))
s3 = float(input('Inserte longitud3 del triangulo:'))

s = (s1+s2+s3)
print(math.sqrt (s*s-s1*s-s2*s-s3))