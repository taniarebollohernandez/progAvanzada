segundos = float(input('Inserte segundos:'))

dia = float(86400)
hora = float(3600)
minuto = float(60)

a = (int(segundos / dia))
b = (segundos % dia)

c = (int(b / hora))
d = (b % hora)

e = (int(d / minuto))
f = (d % minuto)

print('\n %d:%02d:%02d:%02d.' %(a,c,e,f))









