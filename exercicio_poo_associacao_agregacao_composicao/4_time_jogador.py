class Jogador:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
        
class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        return [jogador.nome for jogador in self.jogadores]

time = Time("Seleção Brasileira")
jogador1 = Jogador("Neymar", "Atacante")
jogador2 = Jogador("Alisson", "Goleiro")

time.adicionar_jogador(jogador1)
time.adicionar_jogador(jogador2)
print(f"Jogadores do time {time.nome}: {time.listar_jogadores()}")