from abc import ABC, abstractmethod

class Ligavel(ABC):
    def __init__(self):
        ...
    
    @abstractmethod
    def ligar(self):
        ...
    
class Desligavel(ABC):
    def __init__(self):
        ...
        
    @abstractmethod
    def desligar(self):
        ...

class Computador(Ligavel, Desligavel):
    def __init__(self):
        super().__init__()
        
    def ligar(self):
        print("Computador está ligando...")
        
    def desligar(self):
        print("Computador está desligando...")
        
dell_16 = Computador()
dell_16.ligar()
dell_16.desligar()