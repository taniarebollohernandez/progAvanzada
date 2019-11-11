#Exercise 56: Bill de teléfono celular


CARBONIZARSE = '-'

CARBORIZANTE = 50
TEXTO= 50
COSTO = 15.00
TOTAL = 15.00
COSTO_911 = 0.44
TASA_DE_IMPUESTO = 0.05

minutos = int(input('Ingrese la cantidad de tiempo de aire en minutos:\t'))

if minutos > 50:
  extraMinutos = minutos - 50
  extraMinutosCosto = extraMinutos * 0.25
  TOTAL += extraMinutosCosto
  
textos= int(input('Ingrese el número de textos:\t'))

if textos > 50:
  extraTextos = textos - 50
  extraTextosCosto = extraTextos * 0.15
  TOTAL += extraTextosCosto

TOTAL += COSTO_911

IMPUESTO = TASA_DE_IMPUESTO * TOTAL
TOTAL += IMPUESTO

print(CARBONIZARSE * 50)

print('Carga base: $%.2f' % (COSTO))

try:
  print('Cargo por minutos adicionales: $%.2f' % (extraMinutosCosto))

except NameError:
  pass

try:  
  print('Cargo adicional por mensajes de texto: $%.2f' % (extraTextosCosto))

except NameError:
  pass

print('911 Fee: $%.2f' % (COSTO_911))
print('Impuesto: $%.2f' % (IMPUESTO))
print('Total: $%.2f' % (TOTAL))
