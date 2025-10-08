from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def mover(self):
        ...
        
    @abstractmethod
    def parar(self):
        ...
        
class Carro(Transporte):
    def __init__(self):
        super().__init__()
    
    def mover(self):
        print('O carro está se movendo...')
    
    #TypeError: Can't instantiate abstract class Carro without an implementation 
    # for abstract method 'parar'
        
    def parar(self):
        print('O carro está parando...')
        
compass = Carro()
compass.mover()