from abc import ABC, abstractmethod

class Repositorio(ABC):
    def __init__(self):
        super().__init__()
        
    def salvar(self, objeto):
        ...
        
    def buscar(self, id):
        ...
        
class RepositorioMemoria:
    def __init__(self):
        pass
    
    def aumentar_memoria(self):
        print('Aumentando a memória...')
    
ssd = RepositorioMemoria()
ssd.aumentar_memoria()
