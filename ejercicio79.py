

You're using code navigation to jump to definitions or references.
Learn more or give us feedback 

# Ejercicio 79

#Este ejercicio examina el proceso de identificación del valor máximo en una colección de enteros. 

#Cada uno de los enteros se seleccionará aleatoriamente de los números entre 1 y 100. 

#La colección de enteros puede contener valores duplicados, y algunos de los enteros entre 1 y 100 pueden no estar presentes.

#Tómese un momento y piense cómo manejaría este problema en papel. 

#Muchas personas verifican cada número entero en secuencia y se preguntan si el número que están considerando actualmente es mayor que el número más grande que han visto anteriormente. 

#Si es así, se olvidan del número máximo anterior y recuerdan el número actual como el nuevo número máximo. Este es un enfoque razonable y dará como resultado la respuesta correcta cuando el proceso se realice con cuidado. 

#Si realizara esta tarea, ¿cuántas veces esperaría necesitar actualizar el valor máximo y recordar un nuevo número?

#Si bien podemos responder a la pregunta planteada al final del párrafo anterior utilizando la teoría de la probabilidad, 

#vamos a explorarla simulando la situación. Cree un programa que comience seleccionando un número entero aleatorio entre 1 y 100. 

#Guarde este número entero como el número máximo encontrado hasta ahora. Después de que se haya seleccionado el entero inicial, genere 99 enteros aleatorios adicionales entre 1 y 100. 

#Verifique cada entero tal como se genera para ver si es mayor que el número máximo encontrado hasta ahora. Si es así, su programa debería actualizar el número máximo encontrado y contar el hecho de que realizó una actualización. 

#Muestra cada número entero después de generarlo. Incluya una notación con esos enteros que representan un nuevo máximo.

#Después de haber mostrado 100 enteros, su programa debería mostrar el valor máximo encontrado, 

#junto con la cantidad de veces que el valor máximo se actualizó durante el proceso. La salida parcial para el programa se muestra a continuación, con ... representando los enteros restantes que mostrará su programa. 

#Ejecute su programa varias veces. ¿Es la cantidad de actualizaciones realizadas en el valor máximo lo que esperaba?



from random import randrange



piezas = 100

mx_value = randrange(1, piezas + 1)

print(mx_value)



num_updates = 0



for i in range(1, piezas):

    current = randrange(1, piezas + 1)

    if current > mx_value:

        mx_value = current

        num_updates = num_updates + 1

        print(current, '<== Update')

    else:

        print(current)

print('el valor máximo encontrado es:', mx_value )

print('el valor máximo fue actualizar es: ', num_updates, 'veces')