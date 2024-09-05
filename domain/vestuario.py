from domain.produto import Produto

class Vestuario(Produto):
    def __init__(self, nome, codigo, quantidade, preco, descricao, fornecedor):
        super().__init__(nome, codigo, 'Vestuário', quantidade, preco, descricao, fornecedor)