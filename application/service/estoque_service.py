class EstoqueService:
    def __init__(self, estoque_repo):
        self.estoque_repo = estoque_repo

    def adicionar_produto(self, produto):
        self.estoque_repo.salvar_produto(produto)
        movimentacao = {
            'tipo': 'entrada',
            'produto': produto.nome,
            'codigo': produto.codigo,
            'quantidade': produto.quantidade,
            'descricao': f"Adição de {produto.quantidade} unidades do produto {produto.nome} ao estoque."
        }
        self.estoque_repo.registrar_movimentacao(movimentacao)

    def atualizar_produto(self, codigo, quantidade):
        produto = self.estoque_repo.buscar_produto(codigo)
        if produto:
            quantidade_anterior = produto.quantidade
            produto.quantidade = quantidade
            self.estoque_repo.atualizar_produto(produto)
            movimentacao = {
                'tipo': 'atualização',
                'produto': produto.nome,
                'codigo': produto.codigo,
                'quantidade': quantidade - quantidade_anterior,
                'descricao': f"Atualização do produto {produto.nome}: quantidade alterada para {quantidade}."
            }
            self.estoque_repo.registrar_movimentacao(movimentacao)

    def buscar_produto(self, codigo):
        return self.estoque_repo.buscar_produto(codigo)

    def selecionar_todos_produtos(self):
        return self.estoque_repo.selecionar_todos_produtos()

    def registrar_saida(self, codigo, quantidade):
        produto = self.estoque_repo.buscar_produto(codigo)
        if produto and produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
            self.estoque_repo.atualizar_produto(produto)
            movimentacao = {
                'tipo': 'saída',
                'produto': produto.nome,
                'codigo': produto.codigo,
                'quantidade': quantidade,
                'descricao': f"Saída de {quantidade} unidades do produto {produto.nome}."
            }
            self.estoque_repo.registrar_movimentacao(movimentacao)
            return f"Venda registrada e {quantidade} unidades removidas do estoque."
        else:
            return "Estoque insuficiente ou produto não encontrado."
        
    def historico_movimentacao(self):
        """
        Retorna o histórico de movimentações no estoque.
        
        :return: Lista de movimentações registradas no estoque.
        """
        return self.estoque_repo.buscar_movimentacoes()
