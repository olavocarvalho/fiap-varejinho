from domain.eletronicos import Eletronicos

class EletronicosService:
    def __init__(self, eletronicos_repo):
        self.eletronicos_repo = eletronicos_repo

    def criar_eletronico(self, nome, codigo, quantidade, preco, descricao, fornecedor):
        eletronico = Eletronicos(nome, codigo, quantidade, preco, descricao, fornecedor)
        self.eletronicos_repo.criar(eletronico)
        return f"Eletrônico {eletronico.nome} criado com sucesso!"

    def editar_eletronico(self, codigo, nome=None, quantidade=None, preco=None, descricao=None, fornecedor=None):
        eletronico = self.eletronicos_repo.selecionar(codigo)
        if eletronico:
            if nome: eletronico.nome = nome
            if quantidade is not None: eletronico.quantidade = quantidade
            if preco: eletronico.preco = preco
            if descricao: eletronico.descricao = descricao
            if fornecedor: eletronico.fornecedor = fornecedor
            self.eletronicos_repo.editar(eletronico)
            return f"Eletrônico {codigo} atualizado com sucesso!"
        return f"Eletrônico {codigo} não encontrado!"

    def deletar_eletronico(self, codigo):
        eletronico = self.eletronicos_repo.selecionar(codigo)
        if eletronico:
            self.eletronicos_repo.deletar(codigo)
            return f"Eletrônico {eletronico.nome} deletado com sucesso!"
        return f"Eletrônico {codigo} não encontrado!"

    def selecionar_eletronico(self, codigo):
        eletronico = self.eletronicos_repo.selecionar(codigo)
        if eletronico:
            return vars(eletronico)
        return f"Eletrônico {codigo} não encontrado!"

    def selecionar_todos_eletronicos(self):
        eletronicos = self.eletronicos_repo.buscar_todos_eletronicos()
        return [vars(eletronico) for eletronico in eletronicos]
