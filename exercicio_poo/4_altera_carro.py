class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
carro1 = Carro('Jeep', 'Compass', 2019)
print(f'carro1: {carro1.marca}, {carro1.modelo}, {carro1.ano}')
setattr(carro1, 'ano', '2025')
print(f'O novo ano do carro1: {carro1.ano}')
