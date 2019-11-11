#Exercise 55: Frecuencia para nombrar


frecuencia = float(input('Ingrese la frecuencia:'))

categoría = ''

if frecuencia < 3e9:
	categoria = 'ondas de radio'
elif frecuencia >= 3e9 and frecuencia < 3e12:
	categoria = 'microonda'
elif frecuencia >= 3e12 and frecuencai < 4.3e14:
	categoria = 'luz infrarroja'
elif frecuencia >= 4.3e14 and frecuencia< 7.5e14:
	categoria = 'luz visible'
elif frecuencia >= 7.5e14 and frecuencia < 3e17:
	categoria = 'luz ultravioleta'
elif frecuencia >= 3e17 and frecuencia < 3e19:
	categoria = 'rayos-X'
elif frecuencia >= 3e19:
	categoria = 'rayos gamma'
	
if categoria != '':
	print('La frecuencia es categoría:',(category))
else:
	print('La frecuencia es incorrecta.')
