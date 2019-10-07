estatura1 = float(input('Inserte estatura pies:'))
estatura2 = float(input('pulgadas:'))

pie = float(30.48)
pulgadas = float(2.54)

a = int(estatura1*pie)
b = (estatura1 % pie)
c = (b*pulgadas)
print(a+c , 'cm')