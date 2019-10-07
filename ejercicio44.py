dia = float(input('Inserte dia:'))
mes = input('Inserte mes:')

if dia == 1 and mes == 'julio':
    print('Dia de Canada')
elif dia == 1 and mes == 'enero':
    print('Dia de Año Nuevo')
elif dia == 25 and mes == 'diciembre':
    print('Dia de Año Nuevo')
else:
    print('No corresponden a un dia Feriado')