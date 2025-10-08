from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def falar(self):
        ...
        

class Cachorro(Animal):
    def __init__(self):
        super().__init__()
    
    def falar(self):
        print('Latindo...')
        
    
class Gato(Animal):
    def __init__(self):
        super().__init__()
        
    def falar(self):
        print('Miando...')
    
golden = Cachorro()
garfield = Gato()

golden.falar()
garfield.falar()