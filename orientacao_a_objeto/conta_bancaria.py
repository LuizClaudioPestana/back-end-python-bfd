class ContaBancaria:
    def __init__(self, nome, numero_conta, saldo=0):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.operacoes = []
        
    def __str__(self):
        return f'Conta nº {self.numero_conta} do titular {self.nome} com saldo {self.saldo}'
    
    def saque(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente!')
        else:
            self.saldo = self.saldo - valor
        return self.saldo
    
    def deposito(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo
    
conta_luiz = ContaBancaria('Luiz', 123456)
conta_luiz.deposito(100)
print(conta_luiz.saldo)
conta2 = ContaBancaria('Fulano', 7891011)

