from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def area(self):
        ...
        
    @abstractmethod
    def perimetro(self):
        ...
        
class Retangulo(FormaGeometrica):
    def __init__(self):
        super().__init__()
        
    def area(self, b, a):
        self.b = b
        self.a = a
        ar = b * a
        print(f'A Área do retângulo é base({b}) × altura({a}) = {ar}')
    
    def perimetro(self, b, a):
        p = 2*(b + a)
        print(f'A Área do retângulo é base({b}) × altura({a}) = {p}')
        
obj = Retangulo()
obj.area(10, 20)
obj.perimetro(10, 10)