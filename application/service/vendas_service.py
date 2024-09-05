from domain.vendas import Venda

class VendasService:
    def __init__(self, vendas_repo, estoque_service):
        self.vendas_repo = vendas_repo
        self.estoque_service = estoque_service

    def registrar_venda(self, codigo, quantidade, desconto_strategy=None):
        produto = self.estoque_service.buscar_produto(codigo)
        if produto:
            if produto.quantidade >= quantidade:
                preco_total = quantidade * produto.preco
                if desconto_strategy:
                    preco_total = desconto_strategy.aplicar_desconto(preco_total)

                # Registrar a venda
                venda = Venda(codigo, produto.nome, quantidade, preco_total)
                self.vendas_repo.registrar_venda(venda)

                # Registrar a saída do produto do estoque
                self.estoque_service.registrar_saida(codigo, quantidade)

                return f"Venda registrada: {quantidade}x {produto.nome}. Estoque atualizado. Valor total com desconto: R${preco_total:.2f}."
            else:
                return "Estoque insuficiente para realizar a venda."
        else:
            return "Produto não encontrado no estoque."
        
    def buscar_venda(self, codigo):
        """
        Busca uma venda específica pelo código do produto.

        :param codigo: Código do produto vendido.
        :return: Detalhes da venda ou mensagem de erro.
        """
        venda = self.vendas_repo.buscar_venda(codigo)
        if venda:
            return f"Venda de {venda.quantidade}x {venda.nome_produto} por R${venda.valor_total:.2f}."
        else:
            return "Venda não encontrada."

    def buscar_todas_vendas(self):
        """
        Busca todas as vendas registradas.

        :return: Lista de vendas registradas ou uma mensagem de erro caso não haja vendas.
        """
        vendas = self.vendas_repo.buscar_todas_vendas()
        if vendas:
            return [f"Venda de {venda.quantidade}x {venda.nome_produto} por R${venda.valor_total:.2f}." for venda in vendas]
        else:
            return "Nenhuma venda registrada."