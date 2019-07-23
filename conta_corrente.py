from conta import Conta
class ContaCorrente(Conta):
    def __init__(self, titular, agencia, numero, saldo, limite = 10000):
        super().__init__(titular,agencia, Conta, saldo,limite = 10000)

    def saca(self, valor):
        if valor < self._saldo:
            self._saldo -= valor + 0.11
            return True
        else:
            print("Saldo Insuficiente")
            return False
