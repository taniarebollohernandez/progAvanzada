#Exercise 52: Grade Points to Letter Grade

correcto = int(input('ngrese la cantidad de problemas que obtuvo correctamente:'))

if correcto > 0 :
    print ('Entendido!')

total = int(input('Ingrese el número total de problemas en la prueba:'))

if correcto > 0 :
    print ('Entendido!')
    
porciento = correcto / total * 100

if porciento < 65 :
  letra = 'F'
  
if porciento > 65 and porciento < 70 :
  letra = 'D'

if porciento > 69 and porciento < 80 :
  letra = 'C'

if porciento >= 80 and porciento < 90 :
  letra = 'B'

if porciento >= 90 :
  letra = 'A'



print ('Tu porcentaje correcto es:', porciento )

print ('Tu letra es:', letra)
