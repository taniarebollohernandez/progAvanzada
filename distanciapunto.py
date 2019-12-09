#Escribir un programa que calcule la distancia entre dos puntos dadas las coordenadas, de cada punto. El programa deve contener una clase que tenga los atributos 
#(x,y) y un metodo llamado distancia que se encarga de regresar la distancia entre el mismo punto y otro punto.


import math

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distancia(self, otro):
        delta_x = self.x - otro.x
        delta_y = self.y - otro.y
        return math.sqrt((delta_x ** 2) + (delta_y **2))
punto1 = Punto(3,5)
punto2 = Punto(8,1)
print(punto1.distancia(punto1))