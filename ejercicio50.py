veces = int(input("Ingrese la cantidad de veces:\n"))

for contar in range(veces):
  while True:  
    try:
      a = int(input("Ingrese el valor a:\n"))
      b = int(input("Ingrese el valor de b:\n"))
      c = int(input("Ingrese el valor de c:\n"))
      discriminante = b ** 2 - 4 * a * c
      if discriminante < 0:
        print("Numero de raices: 0\n")
      elif discriminante == 0:
        root = (-b + math.sqrt(discriminant)) / (2 * a)
        print("Numero de raices: 1\nRoot: %f\n" % (root))
      elif discriminante > 0:
        root1 = (-b + math.sqrt(discriminante)) / (2 * a)
        root2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print("Numero de raices: 2\nRoots: %f, %f\n" % (root1, root2))
      break
    except ValueError:
      print("ERROR.\n")

blah = input("Presione ENTER para salir.")
