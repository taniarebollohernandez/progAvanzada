mes = input('Introduzca mes:')
dia = float(int(input('Introduzca dia:')))
if mes == 'enero' or mes =='febrero' or mes == 'marzo' or dia >= 20 or dia <=21:
    print('Primavera')

elif mes == 'abril' or mes == 'mayo' or mes == 'junio' and dia >= 21 or dia <=20:
    print('verano')

elif mes == 'julio' or mes =='agosto' or mes == 'septiembre' and dia >= 22 or dia <=21:
    print('otolo')

elif mes == 'octubre' or mes =='noviembre' or mes == 'diciembre' and dia >= 21 or dia <=20:
    print('invierno')

