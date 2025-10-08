from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def falar(self):
        print('Falando...')
        
cachorro = Animal()
cachorro.falar()
#Na programação orientada a objetos, uma classe abstrata serve como modelo para outras classes. 
# Ela não pode ser instanciada diretamente porque contém um ou mais métodos abstratos que não possuem implementação. 
# Esses métodos são declarados, mas não definidos dentro da própria classe abstrata.