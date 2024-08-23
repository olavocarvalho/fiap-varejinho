class Desconto:
    def aplicar(self, produto, percentual):
        novo_preco = produto.preco - produto.preco * (percentual / 100)
        produto.preco = novo_preco
        return f"Desconto aplicado: {produto.nome} agora custa R${produto.preco:.2f}."