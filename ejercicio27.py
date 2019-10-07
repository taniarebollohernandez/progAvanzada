## Calculadora de IMC

masa = float(input('inserte su masa en peso: '))
estatura = float(input('inserte su estatuta en metros: '))

imc = masa/estatura**2

if imc < 16:
    print('tiene delgadez severa')
elif imc >= 16 and imc < 17:
    print('tiene delgadez moderada')
elif imc >= 17 and imc < 18.5:
    print('tiene delgades leve')
elif imc >= 18.5 and imc < 25:
    print('tiene un imc normal')
elif imc >= 25 and imc < 30:
    print('tiene preobesidad')
elif imc >= 30 and imc < 35:
     print('tiene obesidad leve')
elif imc >= 35 and imc < 40:
    print('tiene obesidad media')
elif imc >= 40:
    print('tiene obesidad mordida')
else:
    print('opcion invalida')

print('su imc fue de', imc)