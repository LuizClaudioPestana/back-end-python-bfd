class Mamifero:
    def __init__(self, idade, habitate, som):
        self.idade = idade
        self.habitate = habitate
        self.som = som
        self.prole = 'gestação'
        self.alimentacao_infantil = 'leite'
        
    def som(self):
        return self.som
    
class Morcego(Mamifero):
    def __init__(self, idade, habitate, som, novo_atributo):
        super().__init__(idade, habitate, som)
        
        self.novo_atributo = novo_atributo
    def voa(self):
        print('Voando...')
    
zubate = Morcego(2, 'Ar', som='Emite som')
print(zubate.idade)
print(zubate.habitate)
print(zubate.som)
print(zubate.prole)
zubate.voa()