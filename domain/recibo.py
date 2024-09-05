class Recibo:
    def __init__(self, id_venda, produto, quantidade, valor_total):
        self.id_venda = id_venda
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = valor_total

    def gerar(self):
        return f"Recibo: {self.quantidade}x {self.produto} - Total: R${self.valor_total:.2f}"