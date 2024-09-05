class Estoque:
    def __init__(self):
        self.produtos = {}  # Um dicionário de produtos, onde a chave é o código do produto
        self.movimentacoes = []  # Lista de movimentações de estoque (entradas e saídas)
        self.observadores = []  # Observadores que serão notificados sobre mudanças no estoque

    def adicionar_produto(self, produto):
        self.produtos[produto.codigo] = produto

    def atualizar_produto(self, codigo, quantidade):
        if codigo in self.produtos:
            produto = self.produtos[codigo]
            produto.quantidade = quantidade

    def registrar_movimentacao(self, movimentacao):
        self.movimentacoes.append(movimentacao)

    def notificar_observadores(self, produto):
        for observador in self.observadores:
            observador.atualizar(produto)