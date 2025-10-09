class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        print(f"Motor tipo {self.tipo} criado.")

    def __del__(self):
        print(f"Motor tipo {self.tipo} destruído.")

class Carro:
    def __init__(self, modelo, tipo_motor):
        self.modelo = modelo
        self.__motor = Motor(tipo_motor) 
        print(f"Carro modelo {self.modelo} criado.")

    def __del__(self):
        print(f"Carro modelo {self.modelo} destruído.")

    def ligar(self):
        print(f"O carro {self.modelo} está ligando o motor.")
        
print("Criando o carro")
meu_carro = Carro("Ford Focus", "Flex")

print("\nO carro está sendo usado...")
meu_carro.ligar()

print("\nApagando a referência ao carro")
del meu_carro
