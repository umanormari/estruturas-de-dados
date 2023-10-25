class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular
    
    #metodo get
    def get_saldo(self, saldo): #usando o método property: substituir get_nome por 'saldo'
        return self._saldo
    
    #metodo set
    def set_saldo(self, saldo):
        if (saldo < 0):
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def deposita(self, valor):
        self.saldo += valor

    def extrato(self):
        print("Cliente: ", self._titular, "Saldo atual: R$ ", self._saldo)

    