class Cuenta:
    def __init__(self, monto, usuario, num_cuenta):
        self. monto = monto
        self. usuario = usuario
        self. num_cuenta = num_cuenta
    def depositar(self, cantidad):
        self.monto = self.monto + cantidad
    def retirar(self, cantidad):
        self.monto = self.monto - cantidad
    def imprimirEstado(self):
        print('Banco de la Alegria')
        print('Cliente:', self.usuario)
        print('Cuenta:', self.num_cuenta)
        print('Saldo:', self.monto)

cuenta_francisca = Cuenta(1000,'Tania','1232432')
cuenta_francisca.depositar (1000)
cuenta_francisca.retirar(400)
cuenta_francisca.depositar(50)
cuenta_francisca.imprimirEstado()
        
