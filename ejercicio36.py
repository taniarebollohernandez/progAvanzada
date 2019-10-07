import re
n = input('Inserte una letra del alfabeto:')

if n == n.lower():
    if re.match("a|e|i|o|u|y",n):
        print('Es una vocal')
    else:
        print('Es una consonante')
