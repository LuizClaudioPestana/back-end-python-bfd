class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial
    
    def get__saldo(self):
        return self.__saldo
    
    def set__saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
        else:
            print('Erro: O saldo não pode ser um valor negativo')
            
        
nova_conta = ContaBancaria()
print(f'Seu Saldo inicial é: R${nova_conta.get__saldo()}')
nova_conta.set__saldo(1000)
print(f'Seu saldo após o depósito é: R${nova_conta.get__saldo()}')
nova_conta.set__saldo(-500)