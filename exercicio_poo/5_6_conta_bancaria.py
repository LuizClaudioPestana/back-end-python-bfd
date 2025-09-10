class ContaBancaria:
    def __init__(self, titular, saldo=500):
        self.titular= titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f'Seu saldo atual é: {self.saldo}')
        return self.saldo

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente!')
        else:
            self.saldo = self.saldo - valor
            print(f'Seu saldo atual é: {self.saldo}')
        return self.saldo
    
class ContaCorrente(ContaBancaria):
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo = self.saldo - valor
            return True 

conta1 = ContaBancaria('Luiz')
conta1.sacar(501)
conta1.sacar(500)
conta1.depositar(500)

conta2 = ContaCorrente('Cláudio')
print(conta2.sacar(501))
print(conta2.sacar(500))