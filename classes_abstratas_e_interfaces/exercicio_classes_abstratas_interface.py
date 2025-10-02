# 1 - Crie uma classe abstrata Pessoa que tenha os métodos: Falar, Andar e Comer e 
# subclasses funcionário e aluno que herde as características e métodos de Pessoa.
#instancie um objeto para cada subclasse.
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def falar(self):
        return print(f"{self.nome} está falando")

    @abstractmethod
    def andar(self):
        return print(f"{self.nome} está andando")

    @abstractmethod
    def comer(self):
        return print(f"{self.nome} está comendo")

class Funcionario(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
    
    def falar(self):
        return super().falar()
    
    def andar(self):
        return super().andar()
    
    def comer(self):
        return super().comer()

class Aluno(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        
    def falar(self):
        return super().falar()
    
    def andar(self):
        return super().andar()
    
    def comer(self):
        return super().comer()


novo_funcionario = Funcionario('O funcionário Luiz')
novo_funcionario.andar()
novo_funcionario.falar()
novo_funcionario.comer()    

novo_aluno = Aluno('O aluno João')
novo_aluno.falar()
novo_aluno.andar()
novo_aluno.comer()
    
       
# 2 - Usando o mesmo exemplo do exercício anterior, converta a classe Pessoa em uma interface.

class Pessoa(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def falar(self):
        pass

    @abstractmethod
    def andar(self):
        pass

    @abstractmethod
    def comer(self):
        pass