from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def processar(self, valor):
        pass
    
class CartaoCredito(Pagamento):
    
    def processar(self, valor):
        print(f"Processando pagamento de R${valor:.2f} com cartão.")
        return True
    
class Boleto(Pagamento):
    def __init__(self):
        super().__init__()
    def processar(self, valor):
        print(f"Processando pagamento de R${valor:.2f} com Boleto.")

utilizando_cartao = CartaoCredito()
utilizando_cartao.processar(100)

utilizando_boleto = Boleto()
utilizando_boleto.processar(200)