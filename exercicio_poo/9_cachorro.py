class Cachorro:
    
    especie='Canis familiaris'
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
dog1 = Cachorro('Priya', 4)
dog2 = Cachorro('Marley', 7)

print("Acessando pela classe:", Cachorro.especie)

print("Acessando pelo objeto (dog1):", dog1.especie)
print("Acessando pelo objeto (dog2):", dog2.especie)