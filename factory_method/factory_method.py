from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def tipo(self) -> str:
        pass

class Carro(Veiculo):
    def tipo(self) -> str:
        return "Dirigindo um carro!"

class Moto(Veiculo):
    def tipo(self) -> str:
        return "Pilotando uma moto!"
    
class VeiculoFactory(ABC):
    @abstractmethod
    def criar_veiculo(self) -> Veiculo:
        pass
    
class CarroFactory(VeiculoFactory):
    def criar_veiculo(self) -> Veiculo:
        return Carro()
    
class MotoFactory(VeiculoFactory):
    def criar_veiculo(self) -> Veiculo:
        return Moto()
    
def cliente(factory: VeiculoFactory) -> None:
    veiculo = factory.criar_veiculo()
    print(veiculo.tipo())
    
if __name__ == "__main__":
    print("Usando a fábrica de carros:")
    cliente(CarroFactory())
    
    print("\nUsando a fábrica de motos:")
    cliente(MotoFactory())