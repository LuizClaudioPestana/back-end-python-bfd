class Comodo:
    def __init__(self, nome):
        self.nome = nome
        print(f"O cômodo {self.nome} foi criado.")

class Casa:
    def __init__(self):
        self.comodos = []
        
        self.comodos.append(Comodo("Sala"))
        self.comodos.append(Comodo("Cozinha"))
        self.comodos.append(Comodo("Quarto"))
        self.comodos.append(Comodo("Banheiro"))
        
        print("A casa foi construída com todos os cômodos.")

    def mostrar_comodos(self):
        print(f"\nOs cômodos da casa são:")
        for comodo in self.comodos:
            print(f"- {comodo.nome}")

minha_casa = Casa()
minha_casa.mostrar_comodos()
