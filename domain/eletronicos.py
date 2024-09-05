from domain.produto import Produto

class Eletronicos(Produto):
    def __init__(self, nome, codigo, quantidade, preco, descricao, fornecedor):
        # A categoria "Eletrônicos" é definida diretamente
        super().__init__(nome, codigo, 'Eletrônicos', quantidade, preco, descricao, fornecedor)
