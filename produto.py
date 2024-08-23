class Produto:
    def __init__(self, nome, codigo, categoria, quantidade, preco, descricao, fornecedor):
        self.nome = nome
        self.codigo = codigo
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.descricao = descricao
        self.fornecedor = fornecedor

    def criar(self):
        return f"Produto {self.nome} criado com sucesso!"

    def editar(self, nome=None, categoria=None, quantidade=None, preco=None, descricao=None, fornecedor=None):
        if nome: self.nome = nome
        if categoria: self.categoria = categoria
        if quantidade is not None: self.quantidade = quantidade
        if preco: self.preco = preco
        if descricao: self.descricao = descricao
        if fornecedor: self.fornecedor = fornecedor
        return f"Produto {self.codigo} atualizado com sucesso!"

    def deletar(self):
        return f"Produto {self.nome} deletado com sucesso!"

    def selecionar(self):
        return vars(self)

    @staticmethod
    def selecionar_todos(produtos):
        return [produto.selecionar() for produto in produtos]