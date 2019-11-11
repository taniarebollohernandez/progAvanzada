año = int(input("Iserta tu año de nacimiento: "))
if (año - 2000) % 12 == 0:
    signo = 'Dragon'
elif (año - 2000) % 12 == 1:
    signo = 'Vivora'
elif (año - 2000) % 12 == 2:
    signo = 'Caballo'
elif (año - 2000) % 12 == 3:
    signo = 'oveja'
elif (año - 2000) % 12 == 4:
    signo = 'chango'
elif (año - 2000) % 12 == 5:
    signo = 'gallo'
elif (año - 2000) % 12 == 6:
    signo = 'perro'
elif (año - 2000) % 12 == 7:
    signo = 'cerdo'
elif (año - 2000) % 12 == 8:
    signo = 'Rata'
elif (año - 2000) % 12 == 9:
    signo = 'Buey'
elif (año - 2000) % 12 == 10:
    signo = 'Tigre'
else:
    signo = 'liebre'

print("Tu signo es :",signo)