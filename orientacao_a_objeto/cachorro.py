class Cachorro:
    especie = 'Canis lupus familiaris'
    def __init__(self, nome, raca, idade):
        self.especie = 'Canis lupus familiaris'
        self.nome = nome
        self.raca = raca
        self.idade = idade
    
    def latir(self):
        print('Au au auuu')
    
    def correr(self, metros):
        print(f'correu {self.correr} metros')
    
dog = Cachorro('Marley', 'labrador', 3)
dog.correr(50)
print(dog.correr(50))