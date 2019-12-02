class Cuenta:
    def __init__(self, monto):
        self. monto = monto
    def depositar(self, cantidad):
        self.monto = self.monto + cantidad
        print('Depositaste', cantidad, 'Tu saldo es:', self.monto)
    def retirar(self, cantidad):
        self.monto = self.monto - cantidad
        print('Retiraste', cantidad, 'Tu saldo es:', self.monto)

cuenta_francisca = Cuenta(100)
cuenta_francisca.depositar (1000)
cuenta_francisca.retirar(400)


cuenta_jose = Cuenta(100)
cuenta_jose.retirar(100)

cuenta_juan = Cuenta(3000)
cuenta_juan.depositar(567.98)
cuenta_juan.retirar(1256)

        