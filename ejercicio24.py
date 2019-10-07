# Ejercicio 24. 



dias = float(input('cuantos dias: '))
horas = float(input('cuantas horas: '))
min = float(input('cuantos minutos: '))
seg = float(input('cuantos segundos: '))

c = float(min*60)
a = float(dias*86400)

b = float(horas*3600)



print('los segundos en total:', a+b+c+seg)
