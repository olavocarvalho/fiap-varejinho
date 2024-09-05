from domain.produto import Produto

class ProdutoService:
    def __init__(self, produto_repo):
        self.produto_repo = produto_repo

    def criar_produto(self, nome, codigo, categoria, quantidade, preco, descricao, fornecedor):
        produto = Produto(nome, codigo, categoria, quantidade, preco, descricao, fornecedor)
        self.produto_repo.criar(produto)
        return f"Produto {produto.nome} criado com sucesso!"

    def editar_produto(self, codigo, nome=None, categoria=None, quantidade=None, preco=None, descricao=None, fornecedor=None):
        produto = self.produto_repo.selecionar(codigo)
        if produto:
            if nome: produto.nome = nome
            if categoria: produto.categoria = categoria
            if quantidade is not None: produto.quantidade = quantidade
            if preco: produto.preco = preco
            if descricao: produto.descricao = descricao
            if fornecedor: produto.fornecedor = fornecedor
            self.produto_repo.editar(produto)
            return f"Produto {codigo} atualizado com sucesso!"
        return f"Produto {codigo} não encontrado!"

    def deletar_produto(self, codigo):
        produto = self.produto_repo.selecionar(codigo)
        if produto:
            self.produto_repo.deletar(codigo)
            return f"Produto {produto.nome} deletado com sucesso!"
        return f"Produto {codigo} não encontrado!"

    def selecionar_produto(self, codigo):
        produto = self.produto_repo.selecionar(codigo)
        if produto:
            return vars(produto)
        return f"Produto {codigo} não encontrado!"

    def selecionar_todos_produtos(self):
        produtos = self.produto_repo.selecionar_todos()
        return [vars(produto) for produto in produtos]
