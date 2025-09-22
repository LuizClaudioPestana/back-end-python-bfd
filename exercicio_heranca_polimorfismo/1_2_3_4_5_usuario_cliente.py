class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def exibir_informacoes(self):
        print(f'O nome do cliente é {self.nome} e seu e-mail {self.email}')
        
    def saudacao(self):
        print('Olá, USUÁRIO!')

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo
    
    def saudacao(self):
        print('Olá, CLIENTE!')
        
class Funcionario(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

class Gerente(Funcionario):
    def __init__(self, nome, email, maiorSalario):
        super().__init__(nome, email)
        self.maiorSalrio = maiorSalario
        

cliente1 = Cliente('Luiz', 'luiz@teste.com', '100')
print(cliente1.nome)
print(cliente1.email)
cliente1.exibir_informacoes()
cliente1.saudacao()

novo_gerente = Gerente('João', 'joao@gerente.com', maiorSalario='Aumento')
print(novo_gerente.nome)
print(novo_gerente.email)
print(novo_gerente.maiorSalrio)