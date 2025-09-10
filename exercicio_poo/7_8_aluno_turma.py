class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        
    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"
        
class Turma:
    def __init__(self):
        self.lista_alunos = []
    
    def adicionar_alunos(self, aluno):
        self.lista_alunos.append(aluno)
        
    def listar_alunos(self):
        for aluno in self.lista_alunos:
            print(f"Nome: {aluno.nome}, Nota: {aluno.nota}")
            
nova_turma = Turma()    

aluno1 = Aluno('Luiz', 10)
aluno2 = Aluno('Bianca', 10)
aluno3 = Aluno('Heraldo', 9)
print(aluno1)
print(aluno2)
print(aluno3)

nova_turma.adicionar_alunos(aluno1)
nova_turma.adicionar_alunos(aluno2)
nova_turma.adicionar_alunos(aluno3)

nova_turma.listar_alunos()
