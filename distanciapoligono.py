#modiifar el programa anterior para que calule, el perimetro de un poligono que tiene 4 vertices 
import math

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distancia(self, otro):
        delta_x = self.x - otro.x
        delta_y = self.y - otro.y
        return math.sqrt((delta_x ** 2) + (delta_y **2))
punto1 = Punto(0,0)
punto2 = Punto(1,0)
punto3 = Punto(1,1)
punto4 = Punto(0,1)
print(punto1.distancia(punto2) + punto1.distancia(punto4) + punto4.distancia(punto3) + punto2.distancia(punto3))