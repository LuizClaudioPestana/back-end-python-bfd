class Pessoa:
    def __init__(self, nome, data_de_nascimento, cpf_inicial, identidade_inicial):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.__cpf = cpf_inicial
        self.__identidade = identidade_inicial
    
    def get__cpf(self):
        return self.__cpf
    
    def get__identidade(self):
        return self.__identidade
    
    def set__cpf(self, novo_cpf):
        if novo_cpf == 11 or novo_cpf != str:
            self.__cpf = novo_cpf
        else:
            print('Informe um número válido!')
    
    def set__identidade(self, nova_identidade):
        if nova_identidade == 7 or nova_identidade != str:
            self.__identidade = nova_identidade
        else:
            print('Informe um número válido!')
            
pessoa = Pessoa('Luiz', '06/01/1995', 12345678990, 9040358)
print(f'Acessando o CPF inicial: {pessoa.get__cpf()}')
pessoa.set__cpf(98765432112)
print(f'Acessando o CPF após alterar: {pessoa.get__cpf()}')
print(f'Acessando a Identidade inicial: {pessoa.get__identidade()}')
pessoa.set__identidade(1234567)
print(f'Acessando a Identidade após alterar: {pessoa.get__identidade()}')