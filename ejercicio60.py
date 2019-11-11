import random

giro = random.randint(0, 37)

if giro == 0:
	if random.randint(0, 2) == 0:
		print("paga 00")
	else:
		print("paga 0")
		
else:
	print("El giro resultó en {}...".format(giro))

	print("paga {}".format(giro))
	
	if giro == 1 or giro == 3 or giro == 5 or giro == 7 or giro == 9 or giro == 12 or giro == 14 or giro == 16 or giro == 18 \
	or giro == 19 or giro == 21 or giro == 23 or giro == 25 or giro == 27 or giro == 30 or giro == 32 or giro == 34 or giro == 36:
		print("paga rojo")
	else:
		print("paga negro")
		
	if giro > 0:
		if giro % 2 == 0:
			print("paga par")
		else:
			print("Paga impar")
	
	if giro >= 1 and giro <= 18:
		print("paga 1 a 18")
	elif giro >= 19 and giro < 36:
		print("paga 19 a 36")
