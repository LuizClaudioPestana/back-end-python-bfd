from abc import ABC, abstractmethod

class Imprimivel(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def imprimir(self):
        ...
        
class Exportavel(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod    
    def exportar(self):
        ...
        
class Relatorio(Imprimivel, Exportavel):
    def __init__(self):
        super().__init__()
    
    def imprimir(self):
        print('O relatório está imprimindo...')
        
    def exportar(self):
        print('O relatório está exportando...')
        
faturamento_mensal = Relatorio()
faturamento_mensal.imprimir()
faturamento_mensal.exportar()