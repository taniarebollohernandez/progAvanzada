# Ejercicio 78.
#Esciba un programaque convierta un numero decimal (base 10) que
#inserte un usuario como numero entero y despues use el 
#algoritmo de division mostrado para realizar la conversion.
#Cuando el algoritmo se complete el resultado debera contener
#la representacion del numero en binario. Despues se debera 
#desplegar el resultado con el mensaje apropiado.
#Sea resultado una variable string vacia.
#Sea q un nnumero entero a convertir repetir:
#+ Sea r igual al residuo cuando q es dividido entre 2.
#+ Convertir r a string y agregarlo al comienzo de resultado.
#+ Dividir q entre 2, eliminar cualquier residuo y guardar el 
#resultado y guardar el resultado de nuevo en q hasta que q
# sea cero.


#Ciclo de repeticion For, while loop

resultado = ''
q = int(input('inserte el numero '))

r = q % 2
resultado = str(r) + resultado
q = q // 2

while q > 0:
    r = q % 2   
    resultado = str (r) + resultado
    q = q // 2


print('el numero binario es', resultado)



#.append() guarda en una lista
#resultado.append(r)

#while comando de ciclo