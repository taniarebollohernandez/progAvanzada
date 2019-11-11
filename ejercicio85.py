#ejercicio 85
#convertir un entelo a un numero cardinal
#la spalabras como primero, segundo, tercero y cuarto son llamas 
#tambien como numeros cardinales.
#En este ejercicio debe de escribir una funcion que tome un numero entero
#como su unico parameto y regrese una cadena de caracteres
#con la palabra cardinal del numero entero insertado . Su funcion debe 
#manejar los numeros enteros entre el 1 y el 12 y debe regresar 
#su correspondiente en numero cardinal. Incluya un programa principal que 
#demuestre su funcion desplegando cada entero del 1 al 12 y su numerocordinal.




def numero(articulos):
    pres = 195.00
    if d == 1:
        print('Primero')
    elif d == 2:
        print('Segundo')
    elif d == 3:
        print('tercero')
    elif d == 4:
        print('cuarto')
    elif d == 5:
        print('qunto')
    elif d == 6:
        print('sexto')
    elif d == 7:
        print('septimo')
    elif d == 8:
        print('octavo')
    elif d == 9:
        print('noveno')
    elif d == 10:
        print('decimo')
    elif d == 11:
        print('onceavo')
    elif d == 12:
        print('doceavo')

    return pres
d = float(input('Inserte numero :'))
final = numero(d)
