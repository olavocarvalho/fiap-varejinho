from eletronicos import Eletronicos
from vestuario import Vestuario
from estoque import Estoque
from vendas import Vendas
from relatorios import Relatorios

class GestorLoja:
    def __init__(self, estoque, vendas, relatorios):
        self.estoque = estoque
        self.vendas = vendas
        self.relatorios = relatorios

    def adicionar_produto(self, produto):
        return self.estoque.adicionar(produto)

    def remover_produto(self, codigo):
        return self.estoque.remover(codigo)

    def atualizar_produto(self, codigo, quantidade):
        return self.estoque.atualizar(codigo, quantidade)

    def registrar_venda(self, codigo, quantidade, desconto_strategy=None):
        return self.vendas.registrar(codigo, quantidade, desconto_strategy)

    def gerar_relatorio_vendas(self):
        return self.relatorios.relatorio_vendas()

    def gerar_relatorio_estoque(self):
        return self.relatorios.relatorio_estoque()

    def gerar_historico_movimentacao(self):
        return self.relatorios.historico_movimentacao()

    def verificar_alertas_estoque(self):
        return self.estoque.alertar()