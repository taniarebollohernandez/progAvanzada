class Triangulo:
    def __init__(self, angulo1, angulo2, angulo3):
        self. angulo1 = angulo1
        self. angulo2 = angulo2
        self. angulo3 = angulo3
    def checar_angulos(self):
        a = self.angulo1 + self.angulo2 + self.angulo3
        if a == 180:
            print('True')
        else:
            print('False')

mitriangulo1 = Triangulo(90, 30, 60)
mitriangulo2 = Triangulo(120, 40, 90)
mitriangulo1.checar_angulos()
mitriangulo2.checar_angulos()