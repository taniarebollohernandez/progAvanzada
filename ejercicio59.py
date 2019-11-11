cuerda = input('Introduce la cadena:')

superior= False
alfa = False
antiguo = False
nuevo = False

if cuerda[0].issuperior() == True and cuerda[1].issuperior() == True and cadena[2].issuperior() == True:
  superior = True
  

if cuerda[0].isalfa() == True and cuerda[1].isalfa() == True and cadena[2].isalfa() == True and cuerda[3].isdigito() == True and cadena[4].isdigito() == True and cadena[5].isdigito() == True and superior == True:
  antiguo = True
  
  print('Esa es una placa vieja')


if cadena[0].isdigito() == True and cadena[1].isdigito() == True and cadena[2].isdigito() == True and cadena[3].isdigito() == True:
  digito = True

if cadena[4].isalfa() == True and cadena[5].isalfa() == True and cadena[6].isalfa() == True:
  alfa = True

if cadena[4].issuperior() == True and cadena[5].issuperior() == True and cadena[6].issuperior() == True:
  superior2 = True

if alfa == True and superior2 == True and digito == True:
  nuevo = True
  
  print('Esa es una nueva placa')

if antiguo == False and nuevo == False:
    
  print('Eso no es matrícula')
