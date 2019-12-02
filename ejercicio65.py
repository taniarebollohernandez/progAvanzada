from math import tan, pi
n_sides = int(input("Numero de entrada de lados: "))
s_length = float(input("Ingresar la longitud de un lado: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("El area del poligono es: ",p_area)