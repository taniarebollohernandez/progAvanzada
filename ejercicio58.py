año = int(input('Inserte año:'))
mes= int(input('Inserte mes:'))
dia = int(input('Inserte dia:'))

siguiente_año = año
siguiente_mes = mes
siguiente_dia = dia

if mes != 12:
	siguiente_año = año
else:
	if dia != 31:
		siguiente_dia = dia
	else:
		siguiente_dia = dia + 1
		

if mes != 9 and mes != 4 and mes != 6 and mes != 6 and mes != 11:
	if dia != 31:
		siguiente_mes = mes
		siguiente_dia = dia + 1
	else:
		if mes != 12:
			siguiete = mes + 1
		else:
			siguiente_mes = 1
		siguiente_dia = 1
else:
	if dia != 30:
		siguiente_mes = mes
		siguiente_dia = dia + 1
	else:
		if mes != 12:
			siguiente_mes = mes + 1
		else:
			siguiente_mes = 1
		siguiente_dia = 1
		
if mes != 2:
	salto = True

	if año % 400 == 0:
		salto = True
	elif año % 100 == 0 and not año % 400 == 0:
		salto = False 
	elif año % 4 == 0 and not año % 100 == 0 and not año % 400 == 0:
		salto = True
	
	if dia == 28:
		if leap:
			siguiente_mes = mes
			siguiente_dia = dia + 1
		else :
			siguiente_mes = mes + 1
			siguiente_dia = 1
			
	else:
		siguiente_mes = mes
		siguiente_dia = dia + 1
		
print('Siguiente dia es : ', siguiente_año, '-', siguiente_mes,'-' , siguiente_dia)
