#ejercicio 49

mag = float(input('ingrese magnitud: '))


if mag >= 0 and mag < 2:
    print('Micro')
elif mag >= 2 and mag < 3:
    print('Very minor') 
elif mag >= 3 and mag < 4:
    print('Minor')
elif mag >= 4 and mag < 5:
    print('light')
elif mag >= 5 and mag < 6:
    print('Moderate')
elif mag >= 6 and mag < 7:
    print('Strong')
elif mag >= 7 and mag < 8:
    print('Major')
elif mag >= 8 and mag < 10:
    print('Great')
elif mag >= 10:
    print('meteoric')
else:
    print('malo')