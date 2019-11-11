#Exercise 51: Letter Grade to Grade Points

nota = input('¿Cuál es el grado de letra?')
nota = nota.upper()
gpa = 0

while True:
    if nota == 'A+':
        gpa = 4.0
        break
    elif nota == 'A':
        gpa = 4.0
        break
    elif nota == 'A-':
        gpa = 3.7
        break
    elif nota == 'B+':
        gpa = 3.3
        break
    elif nota == 'B':
        gpa = 3.0
        break
    elif nota == 'B-':
        gpa = 2.7
        break
    elif nota == 'C+':
        gpa = 2.3
        break
    elif nota == 'C':
        gpa = 2.0
        break
    elif nota == 'C-':
        gpa = 1.7
        break
    elif nota == 'D+':
        gpa = 1.3
        break
    elif nota == 'D':
        gpa = 1.0
        break
    elif nota == 'F':
        gpa = 0
        break
    else:
        print('Invalida nota.')
        nota = input('¿Cuál es el grado de letra?')
        nota = nota.upper()
        gpa = 0 
        
print()
print('puntos de calificación: ', str(gpa))
