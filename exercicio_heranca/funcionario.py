class Pessoa:
    def __init__(self, nome, idade, cpf, cor_cabelo, cor_olhos):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cor_cabelo = cor_cabelo
        self.cor_olhos = cor_olhos
        

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, cor_cabelo, cor_olhos):
        super().__init__(nome, idade, cpf, cor_cabelo, cor_olhos)