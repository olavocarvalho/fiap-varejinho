class Estoque:
    def __init__(self):
        self.produtos = {}
        self.movimentacoes = []
        self.observadores = []

    def adicionar(self, produto):
        self.produtos[produto.codigo] = produto
        # Registrar movimentação de adição
        self.movimentacoes.append({
            'tipo': 'adicionar',
            'produto': produto.nome,
            'codigo': produto.codigo,
            'quantidade': produto.quantidade,
            'descricao': f"Adição de {produto.quantidade} unidades do produto {produto.nome} ao estoque."
        })
        return f"Produto {produto.nome} adicionado ao estoque!"

    def remover(self, codigo):
        if codigo in self.produtos:
            produto = self.produtos.pop(codigo)
            # Registrar movimentação de remoção
            self.movimentacoes.append({
                'tipo': 'remover',
                'produto': produto.nome,
                'codigo': produto.codigo,
                'quantidade': produto.quantidade,
                'descricao': f"Remoção do produto {produto.nome} do estoque."
            })
            return f"Produto {produto.nome} removido do estoque!"
        else:
            return "Produto não encontrado no estoque!"

    def atualizar(self, codigo, quantidade):
        if codigo in self.produtos:
            produto = self.produtos[codigo]
            movimentacao_tipo = 'atualizar'
            quantidade_movimentada = abs(produto.quantidade - quantidade)
            descricao = f"Atualização do estoque do produto {produto.nome}. Quantidade alterada para {quantidade} unidades."

            produto.quantidade = quantidade

            # Registrar movimentação de atualização
            self.movimentacoes.append({
                'tipo': movimentacao_tipo,
                'produto': produto.nome,
                'codigo': produto.codigo,
                'quantidade': quantidade_movimentada,
                'descricao': descricao
            })

            return f"Produto {produto.nome} atualizado para {produto.quantidade} unidades no estoque!"
        else:
            return "Produto não encontrado no estoque!"

    def alertar(self):
        alertas = []
        for produto in self.produtos.values():
            if produto.quantidade < 5:
                alertas.append(f"Alerta: O produto {produto.nome} está com estoque baixo ({produto.quantidade} unidades).")
        return alertas

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self, produto):
        for observador in self.observadores:
            observador.atualizar(produto.codigo, produto.quantidade)

    def historico_movimentacao(self):
        relatorio = "Histórico de Movimentação de Estoque:\n"
        for movimentacao in self.movimentacoes:
            relatorio += f"{movimentacao['descricao']}\n"
        return relatorio
