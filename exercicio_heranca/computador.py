class Computador:
    def __init__(self, modelo, processador, qtd_memoria, departamento):
        self.modelo = modelo
        self.processador = processador
        self.qtd_memoria = qtd_memoria
        self.departamento = departamento
        
class ComputadorComPlaca(Computador):
    def __init__(self, modelo, processador, qtd_memoria, departamento, placa_de_video):
        super().__init__(modelo, processador, qtd_memoria, departamento)
        
        self.placa_de_video = placa_de_video