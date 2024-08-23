class Relatorios:
    def __init__(self, vendas, estoque):
        self.vendas = vendas
        self.estoque = estoque

    def relatorio_vendas(self):
        relatorio = "Relatório de Vendas:\n"
        for venda in self.vendas.vendas:
            relatorio += f"Produto: {venda['produto']} - Quantidade: {venda['quantidade']} - Valor Total: R${venda['valor_total']:.2f}\n"
        return relatorio

    def relatorio_estoque(self):
        relatorio = "Relatório de Estoque:\n"
        for produto in self.estoque.produtos.values():
            relatorio += f"Produto: {produto.nome} - Quantidade: {produto.quantidade} - Preço: R${produto.preco:.2f}\n"
        return relatorio

    def historico_movimentacao(self):
        relatorio = "Histórico de Movimentação de Estoque:\n"
        for movimentacao in self.estoque.movimentacoes:
            relatorio += f"{movimentacao['descricao']}\n"
        return relatorio
