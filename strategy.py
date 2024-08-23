from abc import ABC, abstractmethod

class DescontoStrategy(ABC):
    @abstractmethod
    def aplicar_desconto(self, preco):
        pass

class DescontoPercentual(DescontoStrategy):
    def __init__(self, percentual):
        self.percentual = percentual

    def aplicar_desconto(self, preco):
        desconto = preco * (self.percentual / 100)
        return preco - desconto

class DescontoValorFixo(DescontoStrategy):
    def __init__(self, valor):
        self.valor = valor

    def aplicar_desconto(self, preco):
        return max(preco - self.valor, 0)