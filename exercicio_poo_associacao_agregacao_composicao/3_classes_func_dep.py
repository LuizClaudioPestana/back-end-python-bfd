class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def __str__(self):
        return f"Funcionário: {self.nome}, Salário: R${self.salario:.2f}"

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        if funcionario not in self.funcionarios:
            self.funcionarios.append(funcionario)
            print(f"{funcionario.nome} foi adicionado ao departamento {self.nome}.")
        else:
            print(f"{funcionario.nome} já está no departamento {self.nome}.")
            
novo_funcionario = Funcionario("Ana", 3500)
novo_departamento = Departamento("Recursos Humanos")

novo_departamento.adicionar_funcionario(novo_funcionario)
print(novo_funcionario)