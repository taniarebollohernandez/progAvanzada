a = float(input('Inserte denominacion de un billete $: '))

if a == 1:
    print('George Washington')
elif a == 2:
    print('Tomas Jefferson')
elif a == 5:
    print('Abraham Lincoln')
elif a == 10:
    print('Alexander Hamilton')
elif a == 20:
    print('Andrew Jackson')
elif a == 50:
    print('Ulysses S. Grant')
elif a == 100:
    print('Benjamin Franklin')
else:
    print('ERROR')