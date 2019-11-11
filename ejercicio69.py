# Ejercicio 69. Pi

i = 1
j = 0
suma = 0.0
signo = -1
while i <= 30000:
    den = (i+1.0)*(i+2.0)*(i+3.0)
    signo = signo * -1
    suma = suma + (signo * 4.0)/ den
    i = i + 2
    pi_aprox = 3.0 + suma
    j = j + 1
    print('Iteracion: ', 'Pi aprox', pi-aprox)
    

