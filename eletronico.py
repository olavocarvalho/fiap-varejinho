from produto import Produto

class Eletronico(Produto):
    def __init__(self, nome, categoria, quantidade, preco, descricao, fornecedor, voltagem, garantia):
        super().__init__(nome, categoria, quantidade, preco, descricao, fornecedor)
        self.voltagem = voltagem
        self.garantia = garantia

    @classmethod
    def criar(cls, nome, categoria, quantidade, preco, descricao, fornecedor, voltagem, garantia):
        eletronico = cls(nome, categoria, quantidade, preco, descricao, fornecedor, voltagem, garantia)
        cls._produtos.append(eletronico)
        return eletronico

    @classmethod
    def ler(cls, codigo):
        produto = super().ler(codigo)
        if produto and isinstance(cls._produtos[codigo - 1], Eletronico):
            return produto
        return None

    @classmethod
    def atualizar(cls, codigo, nome=None, categoria=None, quantidade=None, preco=None, descricao=None, fornecedor=None, voltagem=None, garantia=None):
        if super().atualizar(codigo, nome, categoria, quantidade, preco, descricao, fornecedor):
            for produto in cls._produtos:
                if produto.codigo == codigo and isinstance(produto, Eletronico):
                    if voltagem is not None:
                        produto.voltagem = voltagem
                    if garantia is not None:
                        produto.garantia = garantia
                    return True
        return False

    @classmethod
    def deletar(cls, codigo):
        for i, produto in enumerate(cls._produtos):
            if produto.codigo == codigo and isinstance(produto, Eletronico):
                del cls._produtos[i]
                return True
        return False

    @classmethod
    def listar(cls):
        return [vars(produto) for produto in cls._produtos if isinstance(produto, Eletronico)]