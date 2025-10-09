class Onibus:
    def __init__(self, placa, rota, capacidade):
        self.placa = placa
        self.rota = rota
        self.capacidade = capacidade
        self.passageiros = []

    def transportar(self, aluno):
        if len(self.passageiros) < self.capacidade:
            self.passageiros.append(aluno.nome)
            print(f"O aluno {aluno.nome} embarcou no ônibus {self.placa} com destino a {self.rota}.")
        else:
            print(f"O ônibus {self.placa} está lotado. O aluno {aluno.nome} não pode embarcar.")

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def pegar_onibus(self, onibus):
        print(f"O aluno {self.nome} está tentando pegar o ônibus...")
        Onibus.transportar(onibus, self)

onibus_da_faculdade = Onibus("ABC-1234", "CDU", 1)

aluno1 = Aluno("João", "2023001")
aluno2 = Aluno("Maria", "2023002")

aluno1.pegar_onibus(onibus_da_faculdade)
aluno2.pegar_onibus(onibus_da_faculdade)


