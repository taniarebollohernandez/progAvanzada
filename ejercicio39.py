sonido = float(input('Inserte nivel de sonido en decibelios:'))

if sonido <=40:
    print('Cuato Tranquilo')
elif sonido >40 and sonido <=70:
    print('Despertador')
elif sonido >70 and sonido <=106:
    print('Cortacesped a gas')
elif sonido >106 and sonido <=130:
    print('Martillo Neumatico')