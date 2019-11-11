#Exercise 57:¿Es un año bisiesto?

while True:
    
  año = int(input('Ingrese el año:\t'))
  
  si = '%d es un año bisiesto.' % (año)
  no = '%d no es un año bisiesto.' % (año)
  
  if año % 400 == 0:
    print(si)
  
  elif año % 100 == 0:
    print(no)
  
  elif año % 4 == 0:
    print(si)
  
  else:
    print(no)
  
  print()
