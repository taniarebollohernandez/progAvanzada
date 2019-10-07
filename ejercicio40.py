lado1 = float(input('Inserte lado1 del triangulo:'))
lado2 = float(input('Inserte lado2 del triangulo:'))
lado3 = float(input('Inserte lado3 del triangulo:'))

if lado1 == lado2 == lado3:
    print('Es un triangulo equilatero')
elif lado1 == lado2:
    print('Es un triangulo isoseles')
elif lado2 == lado3:
    print('Es un traingulo isoseles')
elif lado1 == lado3:
    print('Es un triangulo isoseles')
else:
    print ('Es un triangulo escaleno')