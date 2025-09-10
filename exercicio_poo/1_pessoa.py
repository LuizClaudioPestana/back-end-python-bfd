class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa('João', 20)
print(f'Seu nome é {pessoa1.nome} e sua idade {pessoa1.idade}')
pessoa2 = Pessoa('Luiz', 30)
print(f'Seu nome é {pessoa2.nome} e sua idade {pessoa2.idade}')
