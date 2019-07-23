class Conta:
    def __init__(self, titular,agencia, numero,saldo, limite = 10000):
        self._titular = titular
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo
        self._limite = limite


    @property
    def titular(self):
        return self._titular
    @titular.setter
    def titular(self,titular):
        self._titular = titular


    @property
    def agencia(self):
        return self._agencia
    @agencia.setter
    def agencia(self,agencia):
        self._agencia = agencia


    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self,numero):
        self._numero = numero


    @property
    def saldo(self):
        return self._saldo


    @property
    def limite(self):
        return self._limite


    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if valor < self._saldo:
            self._saldo -= valor
            return True
        else:
            print("Saldo Insuficiente")
            return False


    def transfere_para(self, conta, valor):
        if self.saca(valor) == True:
            conta.deposita(valor)
        else:
            print('Saldo INSUFICIENTE')
