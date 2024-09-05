from domain.relatorios import Relatorio

class RelatorioService:
    def __init__(self, vendas_service, estoque_service, relatorio_repo=None):
        self.vendas_service = vendas_service
        self.estoque_service = estoque_service
        self.relatorio_repo = relatorio_repo  # Opcional: Se quisermos salvar o relatório gerado

    def relatorio_vendas(self):
        relatorio = "Relatório de Vendas:\n"
        vendas = self.vendas_service.buscar_todas_vendas()
        for venda in vendas:
            relatorio += f"{venda}\n"
        
        # Salvar o relatório, se o repositório for configurado
        if self.relatorio_repo:
            self.relatorio_repo.salvar_relatorio(Relatorio("vendas", relatorio))
        
        return relatorio

    def relatorio_estoque(self):
        relatorio = "Relatório de Estoque:\n"
        produtos = self.estoque_service.selecionar_todos_produtos()
        for produto in produtos:
            # Acessando os atributos do produto com a notação de ponto
            relatorio += f"Produto: {produto.nome} - Quantidade: {produto.quantidade} - Preço: R${produto.preco:.2f}\n"
        
        # Salvar o relatório, se o repositório for configurado
        if self.relatorio_repo:
            self.relatorio_repo.salvar_relatorio(Relatorio("estoque", relatorio))
        
        return relatorio

    def historico_movimentacao(self):
        relatorio = "Histórico de Movimentação de Estoque:\n"
        movimentacoes = self.estoque_service.historico_movimentacao()
        for movimentacao in movimentacoes:
            relatorio += f"{movimentacao}\n"
        
        # Salvar o relatório, se o repositório for configurado
        if self.relatorio_repo:
            self.relatorio_repo.salvar_relatorio(Relatorio("movimentacao", relatorio))
        
        return relatorio
