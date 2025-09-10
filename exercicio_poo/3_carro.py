class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
carro1 = Carro('Jeep', 'Compass', 2019)
print(carro1.marca, carro1.modelo, carro1.ano)
carro2 = Carro('Toyota', 'Etios', 2017)
print(carro2.marca, carro2.modelo, carro2.ano)
carro3 = Carro('BMW', 'X4', 2020)
print(carro3.marca, carro3.modelo, carro3.ano)