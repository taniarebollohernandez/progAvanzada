
# Ejercicio 73

#Existen numerosas frases que son palíndromos cuando se ignora el espacio. 

#Los ejemplos incluyen "ir perro", "huir a mí elfo remoto" y "algunos hombres interpretan nueve notas", entre muchos otros. 

#Extienda su solución al Ejercicio 72 para que ignore el espaciado mientras determina si una cuerda es o no un palíndromo. 

#Para un desafío adicional, extienda su solución para que también ignore los signos de puntuación y trate las letras mayúsculas y minúsculas como equivalentes.



linea = input('Introduce la cadena: ')

palindromo = True



for i in range(2, len(linea) // 2):

    if linea[i] != linea[len(linea)-i-1]:

        palindromo = False

if palindromo:

    print(linea,'Es un palindromo')

else:

    print(linea, 'No es un palindromo')