class Vendas:
    def __init__(self, estoque):
        self.estoque = estoque
        self.vendas = []

    def registrar(self, codigo, quantidade, desconto_strategy=None):
        if codigo in self.estoque.produtos:
            produto = self.estoque.produtos[codigo]
            if produto.quantidade >= quantidade:
                preco_total = quantidade * produto.preco
                if desconto_strategy:
                    preco_total = desconto_strategy.aplicar_desconto(preco_total)

                # Registrar venda
                produto.quantidade -= quantidade
                self.vendas.append({
                    'produto': produto.nome,
                    'codigo': produto.codigo,
                    'quantidade': quantidade,
                    'valor_total': preco_total
                })

                # Registrar movimentação de atualização como saída
                self.estoque.atualizar(codigo, produto.quantidade)
                self.estoque.notificar_observadores(produto)
                return f"Venda registrada: {quantidade}x {produto.nome}. Estoque atualizado para {produto.quantidade} unidades. Valor total com desconto: R${preco_total:.2f}."
            else:
                return "Estoque insuficiente para realizar a venda."
        else:
            return "Produto não encontrado no estoque."
