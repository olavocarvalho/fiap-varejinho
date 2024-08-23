class Produto:
    _produtos = []
    _codigo_counter = 1

    def __init__(self, nome, categoria, quantidade, preco, descricao, fornecedor):
        self.codigo = Produto._codigo_counter
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.descricao = descricao
        self.fornecedor = fornecedor
        Produto._codigo_counter += 1

    @classmethod
    def criar(cls, nome, categoria, quantidade, preco, descricao, fornecedor):
        produto = cls(nome, categoria, quantidade, preco, descricao, fornecedor)
        cls._produtos.append(produto)
        return produto

    @classmethod
    def ler(cls, codigo):
        for produto in cls._produtos:
            if produto.codigo == codigo:
                return vars(produto)
        return None

    @classmethod
    def atualizar(cls, codigo, nome=None, categoria=None, quantidade=None, preco=None, descricao=None, fornecedor=None):
        for produto in cls._produtos:
            if produto.codigo == codigo:
                if nome is not None:
                    produto.nome = nome
                if categoria is not None:
                    produto.categoria = categoria
                if quantidade is not None:
                    produto.quantidade = quantidade
                if preco is not None:
                    produto.preco = preco
                if descricao is not None:
                    produto.descricao = descricao
                if fornecedor is not None:
                    produto.fornecedor = fornecedor
                return True
        return False

    @classmethod
    def deletar(cls, codigo):
        for i, produto in enumerate(cls._produtos):
            if produto.codigo == codigo:
                del cls._produtos[i]
                return True
        return False

    @classmethod
    def listar(cls):
        return [vars(produto) for produto in cls._produtos]