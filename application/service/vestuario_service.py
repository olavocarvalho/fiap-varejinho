from domain.vestuario import Vestuario

class VestuarioService:
    def __init__(self, vestuario_repo):
        self.vestuario_repo = vestuario_repo

    def criar_vestuario(self, nome, codigo, quantidade, preco, descricao, fornecedor):
        vestuario = Vestuario(nome, codigo, quantidade, preco, descricao, fornecedor)
        self.vestuario_repo.criar(vestuario)
        return f"Vestuário {vestuario.nome} criado com sucesso!"

    def editar_vestuario(self, codigo, nome=None, quantidade=None, preco=None, descricao=None, fornecedor=None):
        vestuario = self.vestuario_repo.selecionar(codigo)
        if vestuario:
            if nome: vestuario.nome = nome
            if quantidade is not None: vestuario.quantidade = quantidade
            if preco: vestuario.preco = preco
            if descricao: vestuario.descricao = descricao
            if fornecedor: vestuario.fornecedor = fornecedor
            self.vestuario_repo.editar(vestuario)
            return f"Vestuário {codigo} atualizado com sucesso!"
        return f"Vestuário {codigo} não encontrado!"

    def deletar_vestuario(self, codigo):
        vestuario = self.vestuario_repo.selecionar(codigo)
        if vestuario:
            self.vestuario_repo.deletar(codigo)
            return f"Vestuário {vestuario.nome} deletado com sucesso!"
        return f"Vestuário {codigo} não encontrado!"

    def selecionar_vestuario(self, codigo):
        vestuario = self.vestuario_repo.selecionar(codigo)
        if vestuario:
            return vars(vestuario)
        return f"Vestuário {codigo} não encontrado!"

    def selecionar_todos_vestuario(self):
        vestuarios = self.vestuario_repo.buscar_todos_vestuario()
        return [vars(vestuario) for vestuario in vestuarios]