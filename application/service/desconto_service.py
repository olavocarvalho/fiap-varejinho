class DescontoService:
    def __init__(self, desconto_repo):
        self.desconto_repo = desconto_repo

    def aplicar_desconto(self, codigo_produto, percentual):
        produto = self.desconto_repo.buscar_produto(codigo_produto)
        if produto:
            novo_preco = produto.preco - produto.preco * (percentual / 100)
            produto.preco = novo_preco
            self.desconto_repo.atualizar_preco(produto)
            return f"Desconto aplicado: {produto.nome} agora custa R${produto.preco:.2f}."
        else:
            return "Produto não encontrado!"